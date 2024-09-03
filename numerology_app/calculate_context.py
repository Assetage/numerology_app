import json

from faith_code_calculation import calculation
from importlib import resources


def generate_context(name, birthdate):
    name = name.capitalize()
    day, month, year = (
        birthdate.split(".")[0],
        birthdate.split(".")[1],
        birthdate.split(".")[2],
    )

    num11 = int(day[0])
    num12 = int(day[1])
    num13 = int(month[0])
    num14 = int(month[1])
    num15 = int(year[0])
    num16 = int(year[1])
    num17 = int(year[2])
    num18 = int(year[3])

    num1 = sum([num11, num12, num13, num14, num15, num16, num17, num18])

    num21 = int(str(num1)[0])
    num22 = 0 if len(str(num1)) == 1 else int(str(num1)[1])
    num2 = sum(int(i) for i in str(num1))

    if day[0] == "0":
        num31 = int(day)
        num3 = abs(num1 - 2 * num31)
    else:
        num31 = int(day[0])
        num3 = abs(num1 - 2 * num31)

    num4 = sum(int(i) for i in str(num3))
    num41 = int(str(num3)[0])
    num42 = 0 if len(str(num3)) == 1 else int(str(num3)[1])

    pif_nums = birthdate + str(num1) + str(num2) + str(num3) + str(num4)
    for i in pif_nums:
        pif1 = (
            "".join([i for i in pif_nums if i == "1"])
            if "".join([i for i in pif_nums if i == "1"]) != ""
            else "0"
        )
        pif2 = (
            "".join([i for i in pif_nums if i == "2"])
            if "".join([i for i in pif_nums if i == "2"]) != ""
            else "0"
        )
        pif3 = (
            "".join([i for i in pif_nums if i == "3"])
            if "".join([i for i in pif_nums if i == "3"]) != ""
            else "0"
        )
        pif4 = (
            "".join([i for i in pif_nums if i == "4"])
            if "".join([i for i in pif_nums if i == "4"]) != ""
            else "0"
        )
        pif5 = (
            "".join([i for i in pif_nums if i == "5"])
            if "".join([i for i in pif_nums if i == "5"]) != ""
            else "0"
        )
        pif6 = (
            "".join([i for i in pif_nums if i == "6"])
            if "".join([i for i in pif_nums if i == "6"]) != ""
            else "0"
        )
        pif7 = (
            "".join([i for i in pif_nums if i == "7"])
            if "".join([i for i in pif_nums if i == "7"]) != ""
            else "0"
        )
        pif8 = (
            "".join([i for i in pif_nums if i == "8"])
            if "".join([i for i in pif_nums if i == "8"]) != ""
            else "0"
        )
        pif9 = (
            "".join([i for i in pif_nums if i == "9"])
            if "".join([i for i in pif_nums if i == "9"]) != ""
            else "0"
        )

    KR1 = int(day)
    KR2 = 0 if int(day) <= 22 else 22
    KR = KR1 - KR2

    with resources.open_text(
        "numerology_app.data", "health.json", encoding="utf-8"
    ) as f:
        health_text_json = json.load(f)
    health_text = health_text_json[str(KR)]

    with resources.path("numerology_app.pics", f"{KR}.png") as path:
        arcane_pic = str(path)

    with resources.open_text(
        "numerology_app.data", "arcanes.json", encoding="utf-8"
    ) as f:
        arcane_text_json = json.load(f)

    arcane_title = arcane_text_json[str(KR)]["title"]
    arcane_subtitle = arcane_text_json[str(KR)]["subtitle"]
    arcane_description = arcane_text_json[str(KR)]["description"]
    arcane_text = " ".join(arcane_text_json[str(KR)]["text"])

    day_num = int(day)
    month_num = int(month)
    year1, year2, year3, year4 = int(year[0]), int(year[1]), int(year[2]), int(year[3])
    day_month = day_num + month_num
    year_sum = year1 + year2 + year3 + year4
    if year_sum > 22:
        KS1 = day_month + year_sum - 22
    else:
        KS1 = day_month + year_sum
    KS1_subtraction = 22 if KS1 > 22 else 0
    KS1 = KS1 - KS1_subtraction
    KS1 = KS1 if KS1 <= 22 else KS1 - KS1_subtraction

    day1, day2 = int(day[0]), int(day[1])
    month1, month2 = int(month[0]), int(month[1])
    sum_digits = day1 + day2 + month1 + month2 + year1 + year2 + year3 + year4
    KS2_subtraction = 22 if sum_digits > 22 else 0
    KS2 = sum_digits - KS2_subtraction

    metacycle_period1 = 36 - num2
    metacycle_period2 = metacycle_period1 + 9

    if len(str(num1) + str(num2)) == 4 or len(str(num3) + str(num4)) == 4:
        tysyachnyi_code_text = f"{num1}.{num2}.{num3}.{num4} - у Вас тысячный код. Тысячные коды - это знак популярности, известности, высокого карьерного роста. В человеке заложен потенциал послужить положительным примером как минимум для 1000 людей, вести их за собой, вдохновлять! Этот знак дает амбиции, порой гордыню. Чтобы реализовать свою популярность человек должен найти свое направление, предназначение и совершенствоваться в нем достаточное время. Если у человека заниженная самооценка, ему будет сложно реализовать свой знак тысячника."

        with resources.open_text(
            "numerology_app.data", "tysyachnye_kody.json", encoding="utf-8"
        ) as f:
            tysyachnyi_code_text_main_json = json.load(f)
        tysyachnyi_code_text_main1, tysyachnyi_code_text_main2 = "", ""
        if len(str(num1) + str(num2)) == 4:
            tysyachnyi_code_text_main1 = (
                tysyachnyi_code_text_main_json[f"{num1}.{num2}"]
                if f"{num1}.{num2}" in tysyachnyi_code_text_main_json
                else ""
            )
        if len(str(num3) + str(num4)) == 4:
            tysyachnyi_code_text_main2 = (
                tysyachnyi_code_text_main_json[f"{num3}.{num4}"]
                if f"{num3}.{num4}" in tysyachnyi_code_text_main_json
                else ""
            )
        tysyachnyi_code_text_main = " ".join(
            [tysyachnyi_code_text_main1, tysyachnyi_code_text_main2]
        )
        tysyachnyi_code_text = " ".join(
            [tysyachnyi_code_text, tysyachnyi_code_text_main]
        )
    else:
        tysyachnyi_code_text = ""

    with resources.open_text(
        "numerology_app.data", "karm_kod_tysyachnik.json", encoding="utf-8"
    ) as f:
        karm_kod_text_json = json.load(f)
    karm_kod_znak_tys1 = (
        karm_kod_text_json[f"{num1}.{num2}"]
        if f"{num1}.{num2}" in karm_kod_text_json
        else ""
    )
    karm_kod_znak_tys2 = (
        karm_kod_text_json[f"{num3}.{num4}"]
        if f"{num3}.{num4}" in karm_kod_text_json
        else ""
    )

    with resources.open_text(
        "numerology_app.data", "soc_zadachi.json", encoding="utf-8"
    ) as f:
        soc_zadachi_json = json.load(f)
    soc_zadacha = soc_zadachi_json[str(KS1)]

    with resources.open_text(
        "numerology_app.data", "planet_zadachi.json", encoding="utf-8"
    ) as f:
        planet_zadachi_json = json.load(f)
    planet_zadacha = planet_zadachi_json[str(num2)]

    block_num = KR + month_num if KR + month_num <= 22 else KR + month_num - 22

    with resources.open_text(
        "numerology_app.data", "blocks.json", encoding="utf-8"
    ) as f:
        blocks_json = json.load(f)
    block_text = blocks_json[str(block_num)]

    karm_dolg_num = abs(KR - month_num)

    with resources.open_text(
        "numerology_app.data", "karm_dolg.json", encoding="utf-8"
    ) as f:
        karm_dolg_json = json.load(f)
    karm_dolg_title = karm_dolg_json[str(karm_dolg_num)]["title"]
    karm_dolg_text = " ".join(karm_dolg_json[str(karm_dolg_num)]["text"])

    calc_birthdate = "".join(birthdate.split("."))
    results = calculation(calc_birthdate)

    muladkhara, svadkhistana, manipura, anakhata, vishudkha, adzhna = (
        results[0],
        results[1],
        results[2],
        results[3],
        results[4],
        results[5],
    )

    kontur1 = results[6]

    with resources.open_text(
        "numerology_app.data", "phys_cont_meaning.json", encoding="utf-8"
    ) as f:
        phys_cont_table = json.load(f)
    kontur1_text = phys_cont_table[kontur1]

    kontur2 = results[7]
    with resources.open_text(
        "numerology_app.data", "emot_cont_meaning.json", encoding="utf-8"
    ) as f:
        emot_cont_table = json.load(f)
    kontur2_text = emot_cont_table[kontur2]

    kontur3 = results[8]
    with resources.open_text(
        "numerology_app.data", "int_cont_meaning.json", encoding="utf-8"
    ) as f:
        int_cont_table = json.load(f)
    kontur3_text = int_cont_table[kontur3]

    rod_zadacha_num1, rod_zadacha_num2 = results[9], results[10]
    with resources.open_text(
        "numerology_app.data", "zadachi_po_periodam.json", encoding="utf-8"
    ) as f:
        rod_zadacha_json = json.load(f)
    rod_zadacha_text = "\n\n".join(
        rod_zadacha_json[f"{rod_zadacha_num1}/{rod_zadacha_num2}"]
    )

    karm_zadacha_num1, karm_zadacha_num2 = results[11], results[12]
    karm_zadacha_text = "\n\n".join(
        rod_zadacha_json[f"{karm_zadacha_num1}/{karm_zadacha_num2}"]
    )

    karm_zadacha_num1, karm_zadacha_num2 = results[11], results[12]
    karm_zadacha_text = "\n\n".join(
        rod_zadacha_json[f"{karm_zadacha_num1}/{karm_zadacha_num2}"]
    )

    period1_num1, period1_num2 = results[13], results[14]
    period1_text = "\n\n".join(rod_zadacha_json[f"{period1_num1}/{period1_num2}"])

    period2_num1, period2_num2 = results[15], results[16]
    period2_text = "\n\n".join(rod_zadacha_json[f"{period2_num1}/{period2_num2}"])

    period3_num1, period3_num2 = results[17], results[18]
    period3_text = "\n\n".join(rod_zadacha_json[f"{period3_num1}/{period3_num2}"])

    period4_num1, period4_num2 = results[19], results[20]
    period4_text = "\n\n".join(rod_zadacha_json[f"{period4_num1}/{period4_num2}"])

    period5_num1, period5_num2 = results[21], results[22]
    period5_text = "\n\n".join(rod_zadacha_json[f"{period5_num1}/{period5_num2}"])

    if results[23] != "" and results[24] != "":
        period6_num1, period6_num2 = results[23], results[24]
        period6_text = "\n\n".join(rod_zadacha_json[f"{period6_num1}/{period6_num2}"])
    else:
        period6_num1, period6_num2 = results[23], results[24]
        period6_text = "На этот период особых задач нет."

    context = {
        "KR": KR,
        "KR1": KR1,
        "KR2": KR2,
        "KS1": KS1,
        "KS2": KS2,
        "sum_digits": sum_digits,
        "KS2_subtraction": KS2_subtraction,
        "adzhna": adzhna,
        "anakhata": anakhata,
        "arcane_description": arcane_description,
        "arcane_pic": arcane_pic,
        "arcane_subtitle": arcane_subtitle,
        "arcane_text": arcane_text,
        "arcane_title": arcane_title,
        "birthdate": birthdate,
        "block_num": block_num,
        "block_text": block_text,
        "day": day,
        "day1": day1,
        "day2": day2,
        "day_month": day_month,
        "day_num": day_num,
        "health_text": health_text,
        "karm_dolg_num": karm_dolg_num,
        "karm_dolg_text": karm_dolg_text,
        "karm_dolg_title": karm_dolg_title,
        "karm_kod_znak_tys1": karm_kod_znak_tys1,
        "karm_kod_znak_tys2": karm_kod_znak_tys2,
        "karm_zadacha_num1": karm_zadacha_num1,
        "karm_zadacha_num2": karm_zadacha_num2,
        "karm_zadacha_text": karm_zadacha_text,
        "kontur1": kontur1,
        "kontur1_text": kontur1_text,
        "kontur2": kontur2,
        "kontur2_text": kontur2_text,
        "kontur3": kontur3,
        "kontur3_text": kontur3_text,
        "manipura": manipura,
        "metacycle_period1": metacycle_period1,
        "metacycle_period2": metacycle_period2,
        "month": month,
        "month1": month1,
        "month2": month2,
        "month_num": month_num,
        "muladkhara": muladkhara,
        "name": name,
        "num1": num1,
        "num11": num11,
        "num12": num12,
        "num13": num13,
        "num14": num14,
        "num15": num15,
        "num16": num16,
        "num17": num17,
        "num18": num18,
        "num2": num2,
        "num21": num21,
        "num22": num22,
        "num3": num3,
        "num31": num31,
        "num4": num4,
        "num41": num41,
        "num42": num42,
        "period1_num1": period1_num1,
        "period1_num2": period1_num2,
        "period1_text": period1_text,
        "period2_num1": period2_num1,
        "period2_num2": period2_num2,
        "period2_text": period2_text,
        "period3_num1": period3_num1,
        "period3_num2": period3_num2,
        "period3_text": period3_text,
        "period4_num1": period4_num1,
        "period4_num2": period4_num2,
        "period4_text": period4_text,
        "period5_num1": period5_num1,
        "period5_num2": period5_num2,
        "period5_text": period5_text,
        "period6_num1": period6_num1,
        "period6_num2": period6_num2,
        "period6_text": period6_text,
        "pif1": pif1,
        "pif2": pif2,
        "pif3": pif3,
        "pif4": pif4,
        "pif5": pif5,
        "pif6": pif6,
        "pif7": pif7,
        "pif8": pif8,
        "pif9": pif9,
        "pif_nums": pif_nums,
        "planet_zadacha": planet_zadacha,
        "rod_zadacha_num1": rod_zadacha_num1,
        "rod_zadacha_num2": rod_zadacha_num2,
        "rod_zadacha_text": rod_zadacha_text,
        "soc_zadacha": soc_zadacha,
        "svadkhistana": svadkhistana,
        "tysyachnyi_code_text": tysyachnyi_code_text,
        "vishudkha": vishudkha,
        "year": year,
        "year1": year1,
        "year2": year2,
        "year3": year3,
        "year4": year4,
        "year_sum": year_sum,
    }
    return context
