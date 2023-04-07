from manim import *

part = input('Способ выбора оснащения: ')
spl = int(input('Число точек разбиения: '))


def summar(): # вычисление интегральной суммы
    if part == 'left': # для левого оснащения
        c = 0
        for i in range(spl):
            c += (1 / spl) * (np.exp(2 * (i / spl))) #суммируем площади прямоугольничков
        return c
    elif part == 'right': #для правого оснащения
        c = 0
        for i in range(spl):
            c += (1 / spl) * (np.exp(2 * ((i + 1) / spl)))
        return c
    elif part == 'center': #для среднего оснащения
        c = 0
        for i in range(spl):
            c += (1 / spl) * (np.exp(2 * (i / spl + 1 / (spl * 2))))
        return c


class Riemann(Scene):
    def construct(self):
        ax = Axes(  #создаем декартову плоскость и настраиваем ее
            x_range=[0, 2, 0.5],
            y_range=[0, 9, 0.5],
            x_axis_config={"numbers_to_include": np.arange(0, 2)},
            y_axis_config={"numbers_to_include": np.arange(0, 9), 'numbers_with_elongated_ticks': np.arange(0, 9),
                           "font_size": 20}
        )
        labels = ax.get_axis_labels() #подпись осей
        exp = ax.plot(lambda x: np.exp(2 * x), x_range=[0, 1], color=RED) #график функции на заданном промежутке
        exp_label = ax.get_graph_label(exp, label="y=e^{2x} \ [0,1]").next_to(exp, UP) #подпись графика
        exp_rect = ax.get_riemann_rectangles(  #визуализация интегральной суммы
            exp,
            x_range=[0, 1], #диапозон
            dx=1 / spl, #мелкость
            color=(BLUE, GREEN),
            input_sample_type=part, #способ выбора оснащения
            fill_opacity=0.4, #прозрачность
        )
        title = Title( #вывод сведений об интегральной сумме
            f'Split points: {spl}; Equipment: {part}; Integral sum: {summar()}',
            include_underline=False,
            font_size=30,
            color=YELLOW
        ).next_to(ax, UP)

        self.add(title, ax, labels, exp, exp_label) #добавление неподвижных частей
        self.play(Create(exp_rect), run_time=1) #анимация суммы
