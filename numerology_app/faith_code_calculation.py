import json
from importlib import resources


def calculation(birthdate):
    derivative1 = birthdate[0:4]
    derivative2 = birthdate[4:]
    chronicle_product = int(derivative1) * int(derivative2)

    monada_sum = sum(int(i) for i in birthdate)
    monada_red1 = (
        int(str(monada_sum)[0]) + int(str(monada_sum)[1])
        if monada_sum > 9
        else monada_sum
    )
    monada_red2 = (
        int(str(monada_red1)[0]) + int(str(monada_red1)[1])
        if monada_red1 > 9
        else monada_red1
    )

    genus_sum = sum(int(i) for i in derivative1)
    genus_red1 = (
        int(str(genus_sum)[0]) + int(str(genus_sum)[1]) if genus_sum > 9 else genus_sum
    )
    genus_red2 = (
        int(str(genus_red1)[0]) + int(str(genus_red1)[1])
        if genus_red1 > 9
        else genus_red1
    )

    r1 = genus_red2
    r2 = monada_red2

    compensation_sum = r1 + r2
    compensation_red = (
        int(str(compensation_sum)[0]) + int(str(compensation_sum)[1])
        if compensation_sum > 9
        else compensation_sum
    )

    r3 = compensation_red

    p1 = int(str(chronicle_product)[0])
    period11 = int(str(chronicle_product)[1])
    period21 = int(str(chronicle_product)[2])
    period31 = int(str(chronicle_product)[3])
    period41 = int(str(chronicle_product)[4])
    period51 = int(str(chronicle_product)[5])

    chronicle_compensation_sum1 = r2 + period11
    chronicle_compensation_red1 = (
        int(str(chronicle_compensation_sum1)[0])
        + int(str(chronicle_compensation_sum1)[1])
        if chronicle_compensation_sum1 > 9
        else chronicle_compensation_sum1
    )

    chronicle_compensation_sum2 = r2 + period21
    chronicle_compensation_red2 = (
        int(str(chronicle_compensation_sum2)[0])
        + int(str(chronicle_compensation_sum2)[1])
        if chronicle_compensation_sum2 > 9
        else chronicle_compensation_sum2
    )

    chronicle_compensation_sum3 = r2 + period31
    chronicle_compensation_red3 = (
        int(str(chronicle_compensation_sum3)[0])
        + int(str(chronicle_compensation_sum3)[1])
        if chronicle_compensation_sum3 > 9
        else chronicle_compensation_sum3
    )

    chronicle_compensation_sum4 = r2 + period41
    chronicle_compensation_red4 = (
        int(str(chronicle_compensation_sum4)[0])
        + int(str(chronicle_compensation_sum4)[1])
        if chronicle_compensation_sum4 > 9
        else chronicle_compensation_sum4
    )

    chronicle_compensation_sum5 = r2 + period51
    chronicle_compensation_red5 = (
        int(str(chronicle_compensation_sum5)[0])
        + int(str(chronicle_compensation_sum5)[1])
        if chronicle_compensation_sum5 > 9
        else chronicle_compensation_sum5
    )

    if len(str(chronicle_product)) == 7:
        chronicle_compensation_sum6 = r2 + int(str(chronicle_product)[-1])
        chronicle_compensation_red6 = (
            int(str(chronicle_compensation_sum6)[0])
            + int(str(chronicle_compensation_sum6)[1])
            if chronicle_compensation_sum6 > 9
            else chronicle_compensation_sum6
        )
        period61 = int(str(chronicle_product)[6])
        period62 = chronicle_compensation_red6
    else:
        chronicle_compensation_sum6 = ""
        chronicle_compensation_red6 = ""
        period61 = ""
        period62 = chronicle_compensation_red6

    prenatal_compensation_sum = r2 + p1
    prenatal_compensation_red = (
        int(str(prenatal_compensation_sum)[0]) + int(str(prenatal_compensation_sum)[1])
        if prenatal_compensation_sum > 9
        else prenatal_compensation_sum
    )

    intercalary_check = derivative1[:2]
    month_num = derivative1[-2:]
    marker_month = int(month_num)
    year_intercalarity = (
        "Не високосный год" if int(derivative2) % 4 != 0 else "Високосный год"
    )
    with resources.open_text(
        "numerology_app.data", "month_markers.json", encoding="utf-8"
    ) as f:
        intercalarity_table = json.load(f)
    if year_intercalarity == "Високосный год" and month_num == "02":
        marker_days_in_month = intercalarity_table["2 ВГ"]["days"]
    else:
        marker_days_in_month = intercalarity_table[str(marker_month)]["days"]

    base_marker1, base_marker2, base_marker3 = 23, 28, 33

    with resources.open_text(
        "numerology_app.data", "year_markers.json", encoding="utf-8"
    ) as f:
        year_marker_table = json.load(f)
    year_marker1 = year_marker_table[derivative2]["1"]
    year_marker2 = year_marker_table[derivative2]["2"]
    year_marker3 = year_marker_table[derivative2]["3"]

    if year_intercalarity == "Високосный год" and month_num == "01":
        month_marker1 = intercalarity_table["1 ВГ"]["1"]
        month_marker2 = intercalarity_table["1 ВГ"]["2"]
        month_marker3 = intercalarity_table["1 ВГ"]["3"]
    else:
        month_marker1 = intercalarity_table[str(marker_month)]["1"]
        month_marker2 = intercalarity_table[str(marker_month)]["2"]
        month_marker3 = intercalarity_table[str(marker_month)]["3"]

    day_marker1 = marker_days_in_month - int(derivative1[:2])
    day_marker2 = day_marker1
    day_marker3 = day_marker1

    contour_sum1 = year_marker1 + month_marker1 + day_marker1
    contour_sum2 = year_marker2 + month_marker2 + day_marker2
    contour_sum3 = year_marker3 + month_marker3 + day_marker3

    interim_contour1 = contour_sum1 if contour_sum1 <= 23 else contour_sum1 - 23
    interim_contour2 = contour_sum2 if contour_sum2 <= 28 else contour_sum2 - 28
    interim_contour3 = contour_sum3 if contour_sum3 <= 33 else contour_sum3 - 33

    interim_contour1 = (
        interim_contour1 if interim_contour1 <= 23 else interim_contour1 - 23
    )
    interim_contour2 = (
        interim_contour2 if interim_contour2 <= 28 else interim_contour2 - 28
    )
    interim_contour3 = (
        interim_contour3 if interim_contour3 <= 33 else interim_contour3 - 33
    )

    interim_contour1 = (
        interim_contour1 if interim_contour1 <= 23 else interim_contour1 - 23
    )
    interim_contour2 = (
        interim_contour2 if interim_contour2 <= 28 else interim_contour2 - 28
    )
    interim_contour3 = (
        interim_contour3 if interim_contour3 <= 33 else interim_contour3 - 33
    )

    final_contour1 = base_marker1 if interim_contour1 == 0 else interim_contour1
    final_contour2 = base_marker2 if interim_contour2 == 0 else interim_contour2
    final_contour3 = base_marker3 if interim_contour3 == 0 else interim_contour3

    # raschet page finalizing

    p3 = prenatal_compensation_red

    period12 = chronicle_compensation_red1
    period22 = chronicle_compensation_red2
    period32 = chronicle_compensation_red3
    period42 = chronicle_compensation_red4
    period52 = chronicle_compensation_red5
    # period62 = chronicle_compensation_red6

    with resources.open_text(
        "numerology_app.data", "physical_contour.json", encoding="utf-8"
    ) as f:
        physical_contour_table = json.load(f)
    physical_potential = physical_contour_table[str(final_contour1)]["contour"]
    physical_potential_name = physical_contour_table[str(final_contour1)]["name"]

    with resources.open_text(
        "numerology_app.data", "emotional_contour.json", encoding="utf-8"
    ) as f:
        emotional_contour_table = json.load(f)
    emotional_potential = emotional_contour_table[str(final_contour2)]["contour"]
    emotional_potential_name = emotional_contour_table[str(final_contour2)]["name"]

    with resources.open_text(
        "numerology_app.data", "intellectual_contour.json", encoding="utf-8"
    ) as f:
        intellectual_contour_table = json.load(f)
    intellectual_potential = intellectual_contour_table[str(final_contour3)]["contour"]
    intellectual_potential_name = intellectual_contour_table[str(final_contour3)][
        "name"
    ]

    yin = (
        int(physical_potential[:2])
        + int(intellectual_potential[:2])
        + int(intellectual_potential[3:])
    )
    yang = (
        int(physical_potential[3:])
        + int(emotional_potential[:2])
        + int(emotional_potential[3:])
    )

    want_to = abs(yin - yang)
    able_to = int(physical_potential[:2])
    sex_potential = want_to * able_to

    with resources.open_text(
        "numerology_app.data", "reactivity_markers.json", encoding="utf-8"
    ) as f:
        reactivity_table = json.load(f)
    emotional_type = reactivity_table[str(final_contour2)]["type"]
    I = int(reactivity_table[str(final_contour2)]["I"])
    we = int(reactivity_table[str(final_contour2)]["we"])

    final_output = (
        int(physical_potential[:2]),
        int(physical_potential[3:]),
        int(emotional_potential[:2]),
        int(emotional_potential[3:]),
        int(intellectual_potential[:2]),
        int(intellectual_potential[3:]),
        physical_potential_name,
        emotional_potential_name,
        intellectual_potential_name,
        r1,
        r3,
        p1,
        p3,
        period11,
        period12,
        period21,
        period22,
        period31,
        period32,
        period41,
        period42,
        period51,
        period52,
        period61,
        period62,
    )

    return final_output
