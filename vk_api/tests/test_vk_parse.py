import pandas as pd
import os
import pytest
from vk_parse import VkParser

temp_user_token = '3ab836a23ab836a23ab836a22b39afc09b33ab83ab836a25ca2a165f6acc297a94b3c3d'

test_parser_input1 = 'rE9z%KbN&G7qLyDc#TvX2eJ3Pb6ZgH4kC1jWs8L!UQoMfA5hI0'
test_parser_result1 = []
test_parser_input2 = 'oZ7%QcX1sG3mFtPb#JyUwD5kV4eL!N9hR8gAiW6nKpY2dE0SxH7'
test_parser_result2 = [{"texts": "oZ7%QcX1sG3mFtPb#JyUwD5kV4eL!N9hR8gAiW6nKpY2dE0SxH7 https://chat.openai.com/ https://twitter.com/home 1234567890",
                         "likes": 1, "reposts": 0, "comments": 2, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]
test_parser_input3 = 'lM6&vF0xK9pR7iH#QsE3wG5yL4tB1zV!NjUoDcA8fW2rXePbYgZ'
test_parser_result3 = [{"texts": "lM6&vF0xK9pR7iH#QsE3wG5yL4tB1zV!NjUoDcA8fW2rXePbYgZ oewdbvbsaasdx800",
                         "likes": 0, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"},
                         {"texts": "lM6&vF0xK9pR7iH#QsE3wG5yL4tB1zV!NjUoDcA8fW2rXePbYgZ 1234567890_TQCSG",
                         "likes": 1, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"},]
test_parser_input4 = 'qI7cDjG2tY8sN5eL!FmK%hP0zX9fUoR1bVwJ6yW3rA4dSxEgHnB'
test_parser_result4 = [{"texts": "qI7cDjG2tY8sN5eL!FmK%hP0zX9fUoR1bVwJ6yW3rA4dSxEgHnB Patchwerk fat american 胖胖美国人angered hits on armored men对装甲兵的怒吼intentional pain river keeps others safe故意痛苦的河流使他人安全medics focus those who eat fists医务人员将重点放在那些吃拳头的人身上",
                         "likes": 0, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input5 = 'zS3cU4yL!VbW2nGk#E5sX8hM9pF0jI1qA6rP7gDlTfKoBwRdZvYx'
test_parser_result5 = [{"texts": "123214324 zS3cU4yL!VbW2nGk#E5sX8hM9pF0jI1qA6rP7gDlTfKoBwRdZvYx 46443636463",
                         "likes": 0, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input6 = 'jO6eT7sL!mD5xJ2qB9aU3cV8iR0fZ1tP#X4kWgYwHrFyKpNvGhE'
test_parser_result6 = [{"texts": "jO6eT7sL!mD5xJ2qB9aU3cV8iR0fZ1tP#X4kWgYwHrFyKpNvGhE 6565656555656656656565611212121212-0-0-656756",
                         "likes": 0, "reposts": 0, "comments": 1, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input7 = 'kelthuzad 基爾紮紮德 ICE WIZZARD 冰精灵'
test_parser_result7 = [{"texts": "kelthuzad 基爾紮紮德 ICE WIZZARD 冰精灵 circles on ground dangerous 危險地上的圓圈 friends turn enemy 朋友是敵人monster undead appear 怪物不死族出現 wise men apply chains 智者應用鎖鏈",
                         "likes": 0, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input8 = 'Ямч8УвШ5чЙкцЩйюэМрЯЕьжГзФфЦ4ЯЫртВе0ИоХфДь'
test_parser_result8 = [{"texts": "Ямч8УвШ5чЙкцЩйюэМрЯЕьжГзФфЦ4ЯЫртВе0ИоХфДь лол6598тпдлоуц23090г9риммтлолиц56786ьть рпорпортлоьтьтьекг7689лодлоря",
                         "likes": 0, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input9 = 'kP3jC8gY4nH1fI#V6mB5xK0oR2tS9zE7uL!DlGwXyAqMvJpWdFhT'
test_parser_result9 = [{"texts": "kP3jC8gY4nH1fI#V6mB5xK0oR2tS9zE7uL!DlGwXyAqMvJpWdFhT 79878976тмитмсмсчк5768GFDSGdgghju67664n0032x",
                         "likes": 1, "reposts": 1, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input10 = 'iZ0eQ4xW7lL!T3bV6kF5jU1cP2sG9mR8oYdA#NtXhMvBwJgIqHrD'
test_parser_result10 = [{"texts": "iZ0eQ4xW7lL!T3bV6kF5jU1cP2sG9mR8oYdA#NtXhMvBwJgIqHrD GDSGgfdggh6455cxbvn_e32",
                         "likes": 0, "reposts": 1, "comments": 0, "user_id": 858757284,
                         "views": 1, "date": "2024-04-14"}]

test_parser_input11 = 'rS2tD3oA5kW8mJ!X0fN6zV9uH1cB#P7qGyIwRlLgE4dYjTnKvFh'
test_parser_result11 = [{"texts": "rS2tD3oA5kW8mJ!X0fN6zV9uH1cB#P7qGyIwRlLgE4dYjTnKvFh 768776912168989",
                         "likes": 0, "reposts": 0, "comments": 0, "user_id": 858757284,
                         "views": 2, "date": "2024-04-14"}]

@pytest.mark.parametrize("test_input, test_result", [(test_parser_input1, test_parser_result1),
                                                     (test_parser_input2, test_parser_result2),
                                                     (test_parser_input3, test_parser_result3),
                                                     (test_parser_input4, test_parser_result4),
                                                     (test_parser_input5, test_parser_result5),
                                                     (test_parser_input6, test_parser_result6),
                                                     (test_parser_input7, test_parser_result7),
                                                     (test_parser_input8, test_parser_result8),
                                                     (test_parser_input9, test_parser_result9),
                                                     (test_parser_input10, test_parser_result10),
                                                     (test_parser_input11, test_parser_result11)   ])

def test_parser(test_input, test_result):
    parser = VkParser(USER_TOKEN=temp_user_token)
    parser.parse_vk_weekly(query=test_input)
    assert os.path.exists(f'{test_input}.csv')
    df = pd.read_csv(f'{test_input}.csv')
    assert len(df) == len(test_result)
    for expected_row in test_parser_result1:
        assert expected_row in df.to_dict(orient="records")