import os

import pkg_resources
from fpdf import FPDF
from setup_fonts import add_fonts_to_fpdf


class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.background_color = (234, 221, 202)  # almond (234, 221, 202)

    def header(self):
        self._draw_background()
        self._draw_header_content()

    def _draw_background(self):
        self.set_fill_color(*self.background_color)
        self.rect(0, 0, self.w, self.h, "F")

    def _draw_header_content(self):
        # Save current position and settings
        original_y = self.get_y()
        original_font = self.font_family, self.font_style, self.font_size_pt

        self.set_y(10)  # Set to top of the page
        self.set_font("DejaVu", "B", 10)
        self.set_text_color(50, 50, 50)

        text = "nurassyl.kussaiyn"
        instagram_url = "https://www.instagram.com/nurassyl.kussaiyn/"
        utils_pics_dir_path = os.path.join(
            pkg_resources.resource_filename("numerology_app", "pics"), "utils_pics"
        )
        instagram_icon = os.path.join(utils_pics_dir_path, "insta4.png")

        icon_height = self.font_size_pt * 0.7 / 2.835  # Convert pt to mm
        text_width = self.get_string_width(text)
        total_width = icon_height + 5 + text_width
        x_icon = (self.w - total_width) / 2
        x_text = x_icon + icon_height + 0.5

        self.image(instagram_icon, x_icon, self.get_y(), h=icon_height)
        self.link(x_icon, self.get_y(), icon_height, icon_height, instagram_url)

        self.set_xy(x_text, self.get_y())
        self.set_text_color(88, 81, 216)
        self.cell(
            text_width, self.font_size_pt / 2.835, text, 0, 1, "L", link=instagram_url
        )

        # Move cursor below the header
        self.ln(10)

        # Restore original position and settings
        self.set_font(*original_font)

    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "I", 8)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, f"Страница {self.page_no()}", 0, 0, "C")

    def chapter_title(self, title, size=15, style="B"):
        self.set_font("DejaVu", style, size)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, 0, 1, "C")
        self.ln(8)

    def chapter_body(self, body, size=10, style=""):
        self.set_font("DejaVu", style, size)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 6, body)
        self.ln()

    def chapter_small_body(self, body, size=8, style=""):
        self.set_font("DejaVu", style, size)
        self.set_text_color(0, 0, 0)
        self.multi_cell(0, 5, body)
        self.ln()

    def add_image(self, image_path, width=80):
        self.image(image_path, x=(self.w - width) / 2, w=width)
        self.ln(10)

    def add_matrix_table(self, data):
        # Calculate column widths based on page width
        page_width = self.w - 2 * self.l_margin  # Total available width
        col_widths = [page_width / 3] * 3  # Equal width for 3 columns

        digit_height = 10
        desc_line_height = 5

        for row in data:
            max_height = digit_height

            # First pass: calculate max height for this row
            for digit, description in row:
                self.set_font("DejaVu", "", 8)
                desc_lines = self.multi_cell(
                    col_widths[0], desc_line_height, description, split_only=True
                )
                cell_height = digit_height + (len(desc_lines) * desc_line_height)
                max_height = max(max_height, cell_height)

            # Second pass: actually draw the cells
            for i, (digit, description) in enumerate(row):
                x_start = self.get_x()
                y_start = self.get_y()

                # Draw border
                self.cell(col_widths[i], max_height, "", border=1)

                # Add digit
                self.set_xy(x_start, y_start)
                self.set_font("DejaVu", "B", 12)
                self.cell(col_widths[i], digit_height, digit, align="C")

                # Add description
                self.set_xy(x_start, y_start + digit_height)
                self.set_font("DejaVu", "", 8)
                self.multi_cell(col_widths[i], desc_line_height, description, align="C")

                # Move to next cell
                self.set_xy(x_start + col_widths[i], y_start)

            self.ln(max_height)

    def add_standard_table(self, data, col_widths=None):
        # Calculate available width
        page_width = self.w - 2 * self.l_margin

        # If col_widths is not provided, calculate equal widths
        if col_widths is None:
            num_cols = len(data[0])
            col_widths = [page_width / num_cols] * num_cols
        else:
            # Adjust provided col_widths to fit page width
            total_width = sum(col_widths)
            scale_factor = page_width / total_width
            col_widths = [width * scale_factor for width in col_widths]

        for row in data:
            for i, cell in enumerate(row):
                self.set_font("DejaVu", "", 11)
                self.cell(col_widths[i], 10, str(cell), border=1, align="C")
            self.ln()

    def create_numerology_report(self, context):
        self.add_page()

        # Personal Info
        title = (
            f"{context['name']} {context['day']}.{context['month']}.{context['year']}"
        )
        self.chapter_title(title)

        # Pythagoras Matrix
        self.chapter_title("МАТРИЦА ПИФАГОРА")
        pif_descriptions = [
            "Характер, воля, самоуверенность, наличие лидерских качеств.",
            "Энергия.",
            "Интерес человека к чему-либо, стабильность, скорость восприятия; креативность, эпатажность; способность к обучению.",
            "Здоровье, жизненные силы, выносливость, темперамент, физическое тело.",
            "Логика, интуиция, предвидение, рациональность.",
            "Заземленность, практичность; склонность к физическому труду, творчество, способность что-то делать руками.",
            "Благословение небес, удача.",
            "Чувство долга, ответственности, справедливости; терпимость, совесть; интерес к общественной жизни",
            "Память, ум, интуиция.",
        ]
        matrix_data = [
            [
                (f"{context['pif1']}", pif_descriptions[0]),
                (f"{context['pif4']}", pif_descriptions[3]),
                (f"{context['pif7']}", pif_descriptions[6]),
            ],
            [
                (f"{context['pif2']}", pif_descriptions[1]),
                (f"{context['pif5']}", pif_descriptions[4]),
                (f"{context['pif8']}", pif_descriptions[7]),
            ],
            [
                (f"{context['pif3']}", pif_descriptions[2]),
                (f"{context['pif6']}", pif_descriptions[5]),
                (f"{context['pif9']}", pif_descriptions[8]),
            ],
        ]
        self.add_matrix_table(matrix_data)
        digits_explanation = [
            "Нет цифр - качество отсутствует.",
            "Одна цифра - качество развито слабо.",
            "Две цифры - качество развито хорошо. Норма.",
            "Три цифры - качество нестабильно.",
            "Четыре цифры - качество развито очень хорошо.",
            "Пять цифр - качество развито очень сильно и нестабильно.",
            "Шесть и более - перегруз, поэтому ослабление - все равно, что 1 или 2 цифры, и т.д.",
        ]
        self.chapter_small_body("\n".join(digits_explanation), style="I", size=6)
        self.chapter_body(
            "Данные из квадрата Пифагора это рожденный показатель, который склонен к корректировке. Человек в течение всей своей жизни может как развить эти качества, так и ослабить.",
            style="B",
        )
        self.chapter_body(f"По здоровью могут быть {context['health_text']}")

        # Arcane Details
        self.add_page()
        self.chapter_title("АРКАН")
        self.add_image(context["arcane_pic"])
        self.chapter_body(f"{context['KR']} = {context['arcane_title']}", style="B")  #
        self.chapter_body(f"{context['arcane_subtitle']}", style="B")
        if context["arcane_description"] != "":
            self.chapter_body(context["arcane_description"], style="I")
        self.chapter_body(context["arcane_text"], style="")

        # Metacycles
        self.chapter_title("МЕТАЦИКЛЫ")
        metacycle_data = [
            ["Метациклы", "I", "II", "III"],
            ["Аркан", context["KR"], context["KS1"], context["KS2"]],
            [
                "Периоды лет",
                f"0 до {context['metacycle_period1']}",
                f"{context['metacycle_period1']} - {context['metacycle_period2']}",
                f"{context['metacycle_period2']} - дальше",
            ],
        ]
        self.add_standard_table(metacycle_data)

        # Tasks and Karmic Code
        self.add_page()
        self.chapter_title("ЗАДАЧИ")
        if context["tysyachnyi_code_text"] != "":
            self.chapter_body(context["tysyachnyi_code_text"])
        self.chapter_body(
            f"{context['num1']}.{context['num2']} - {context['karm_kod_znak_tys1']}"
        )
        if context["karm_kod_znak_tys2"] != "":
            self.chapter_body(
                f"{context['num3']}.{context['num4']} - {context['karm_kod_znak_tys2']}"
            )
        self.chapter_body("Социальная задача:", style="B")
        self.chapter_body(f"{context['soc_zadacha']}")
        self.chapter_body("Планетарная задача:", style="B")
        self.chapter_body(f"{context['planet_zadacha']}")

        # Blocks
        self.add_page()
        self.chapter_title("БЛОК")
        self.chapter_body(
            "который может препятствовать вам в жизни (именно это убрав, вы сможете реализовать себя):",
            style="I",
        )
        self.chapter_body(context["block_text"])
        self.chapter_body(
            "Если в задачах нужно делать всё, как просят, здесь всё ровно наоборот."
        )
        self.chapter_body("Нужно убрать блок полностью!", style="B")
        self.chapter_body(
            "Если вы уже давно этот момент проработали или не чувствуете подобного - отлично! :) Расчёт дается для того, чтобы мы знали от чего отталкиваться и то, что нужно отработать - отработали, что не нужно - убрали, всё поддается корректировке"
        )

        # Karmic Debt
        self.add_page()
        self.chapter_title("КАРМИЧЕСКИЙ ДОЛГ")
        self.chapter_title("(ошибка из прошлого воплощения)", style="I")
        self.chapter_body("ВАША карма из ПРОШЛОГО воплощения:")
        self.chapter_body(f"{context['karm_dolg_title']}", style="B")
        self.chapter_body(
            "То есть это то, что вы ошибочно сделали в прошлой жизни, и в этой жизни эту карму нужно отработать."
        )
        self.chapter_body(
            "Есть множество вариантов того, как это может проявиться в ЭТОЙ жизни."
        )
        self.chapter_body(context["karm_dolg_text"])

        # Chakra Analysis
        self.add_page()
        self.chapter_title("ЧАКРОАНАЛИЗ")
        self.chapter_body("Наполняемость чакр:", style="B")
        chakra_data = [
            ["ФИЗИЧЕСКИЙ КОНТУР", "ЭМОЦИОНАЛЬНЫЙ КОНТУР", "ИНТЕЛЛЕКТУАЛЬНЫЙ КОНТУР"],
            [
                f"Муладхара – {context['muladkhara']}%",
                f"Манипура – {context['manipura']}%",
                f"Вишудха – {context['vishudkha']}%",
            ],
            [
                f"Свадхистана – {context['svadkhistana']}%",
                f"Анахата – {context['anakhata']}%",
                f"Аджна – {context['adzhna']}%",
            ],
        ]
        self.add_standard_table(chakra_data)
        self.ln()
        self.chapter_body(context["kontur1"], style="B")
        self.chapter_body(context["kontur1_text"])
        self.chapter_body(context["kontur2"], style="B")
        self.chapter_body(context["kontur2_text"])
        self.chapter_body(context["kontur3"], style="B")
        self.chapter_body(context["kontur3_text"])

        # Period Tasks
        self.add_page()
        self.chapter_title("ЗАДАЧИ ПО ЧАКРАМ")
        self.chapter_title("Родовая задача")
        self.chapter_title(
            "(то, что досталось от рода/требует род от вас, действует всю жизнь):",
            style="I",
        )
        self.chapter_body(
            f"{context['rod_zadacha_num1']}({context['rod_zadacha_num2']}): {context['rod_zadacha_text']}"
        )
        self.chapter_title("Кармическая задача")
        self.chapter_body(
            f"{context['karm_zadacha_num1']}({context['karm_zadacha_num2']}): {context['karm_zadacha_text']}"
        )
        self.chapter_title("Задачи по периодам")
        self.chapter_body(
            "Если в стартовом периоде от 1 до 12 лет стоит задача для взрослого, то в этом случае нужно развивать эти чакры, задача никуда не уходит оно переносится на след. период.",
            style="I",
        )
        self.chapter_body(
            f"{context['period1_num1']}({context['period1_num2']}) (1-12 лет):",
            style="B",
        )
        self.chapter_body(context["period1_text"])
        self.chapter_body(
            f"{context['period2_num1']}({context['period2_num2']}) (12-24 лет):",
            style="B",
        )
        self.chapter_body(context["period2_text"])
        self.chapter_body(
            f"{context['period3_num1']}({context['period3_num2']}) (24-36 лет):",
            style="B",
        )
        self.chapter_body(context["period3_text"])
        self.chapter_body(
            f"{context['period4_num1']}({context['period4_num2']}) (36-48 лет):",
            style="B",
        )
        self.chapter_body(context["period4_text"])
        self.chapter_body(
            f"{context['period5_num1']}({context['period5_num2']}) (48-60 лет):",
            style="B",
        )
        self.chapter_body(context["period5_text"])
        self.chapter_body(
            f"{context['period6_num1']}({context['period6_num2']}) (60-до конца жизни):",
            style="B",
        )
        self.chapter_body(context["period6_text"])


def generate_report(context):
    pdf = PDF()
    add_fonts_to_fpdf(pdf)  # Automatically add the fonts
    pdf.create_numerology_report(context)
    output_pdf_dir = "generated_reports"
    os.makedirs(output_pdf_dir, exist_ok=True)
    output_pdf = f'{context["name"].capitalize()}_{context["day"]}{context["month"]}{context["year"]}.pdf'
    pdf.output(os.path.join(output_pdf_dir, output_pdf))
