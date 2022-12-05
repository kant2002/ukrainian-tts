from ukrainian_tts.formatter import preprocess_text


def test_formatter():
    examples = [
        ("Quality of life update", "КВюаліті оф ліфе юпдате"),
        ("Він украв 20000000 $", "Він украв двадцять мільйонів долар"),
        (
            "111 000 000 000 доларів державного боргу.",
            "сто одинадцять мільярдів доларів державного боргу.",
        ),
        (
            "11100000001 доларів державного боргу.",
            "одинадцять мільярдів сто мільйонів один доларів державного боргу.",
        ),
        ("це 19-річне вино.", "це дев'ятнадцять-річне вино."),
        ("10-30-40-50-5-9-5", "десять-тридцять-сорок-п'ятдесят-п'ять-дев'ять-п'ять"),
    ]
    for item in examples:
        assert preprocess_text(item[0]) == item[1]
