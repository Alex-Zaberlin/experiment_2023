from otree.api import *

doc = """
A real-effort trust game
"""


class C(BaseConstants):
    MULTIPLIER = 3
    INSTRUCTIONS_TEMPLATE = 'instructions.html'
    NAME_IN_URL = 'experiment_2023'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    test_answers = [49, 49, 57, 49, 55, 57, 51, 41, 48, 44, 46, 46, 47, 56, 50, 45, 45, 59, 40, 50, 50, 51, 48, 50, 49, 47, 49, 45, 50, 50, 58, 59, 52, 49, 44, 42, 62, 50, 48, 55, 51, 51, 44, 61, 46, 53, 43, 57, 53, 51]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    endowment = models.CurrencyField(initial = cu(0))
    treatment = models.StringField(
        choices=[['T', 'T'], ['NT', 'NT']],
        label='Тритмент',
        widget=widgets.RadioSelect,
    )
    # sent_amount = models.CurrencyField(
    #     min=cu(0),
    #     max=endowment,
    #     doc="""Amount sent by P1""",
    #     label="How much do you want to send to participant B?",
    # )

    sent_amount = models.CurrencyField(
        min=cu(0),
        doc="""Amount sent by P1""",
        label="How much do you want to send to participant B?",
    )



    sent_back_amount = models.CurrencyField(
        min=cu(0),
        doc="""Amount sent back by P2""",
        label="How much do you want to send back?"
    )

    expectations_player1 = models.CurrencyField(
        min=cu(0),
        doc="""Amount sent back by P2""",
        label="Сколько вы ожидаете получить назад?"
    )




class Player(BasePlayer):

    test_score = models.IntegerField(initial = 0)

    expectations_p1_player2 = models.IntegerField(label='Как Вы думаете, сколько баллов набрал за тест Игрок 1?', min=0, max=50)

    expectations_p2_player2 = models.IntegerField(label='Как Вы думаете, сколько баллов Вы набрали бы за тест, если бы писали его?', min=0,
                                                  max=50)

    age = models.IntegerField(label='What is your age?', min=13, max=125)
   # pic = models.IntegerField(label=<img src="{{ static 'matrices_app/task_1.png' }}"/>, min=0, max=100)

    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    # crt_bat = models.IntegerField(
    #     label='''
    #     A bat and a ball cost 22 dollars in total.
    #     The bat costs 20 dollars more than the ball.
    #     How many dollars does the ball cost?'''
    # )
    # crt_widget = models.IntegerField(
    #     label='''
    #     1 0 1 0 1 0 1 0 1 0 <br>
    #     1 0 1 0 1 0 1 0 1 0 <br>
    #     1 0 1 0 1 0 1 0 1 0 <br>
    #     1 0 1 0 1 0 1 0 1 0 <br>
    #     1 0 1 0 1 0 1 0 1 0
    #     '''
    # )
    # crt_lake = models.IntegerField(
    #     label='''
    #     <img src="https://chudo-prirody.com/uploads/posts/2021-08/1628909188_6-p-khitrii-kot-foto-6.jpg" width="500px" />
    #     '''
    #
    # )
    #<img src='../matrices_app/task_1.png' />
    #<img src="{{ '../matrices_app/task_1.png' }}"/>
    #<img src='.C:/Users/kalas/Desktop/Annie/Uni/COURSES/THESIS/1.Endowment_in_dictator_games/Dictator_game/matrices/task_1.png' />
    #<img src="{{ '.C:/Users/kalas/Desktop/Annie/Uni/COURSES/THESIS/1.Endowment_in_dictator_games/Dictator_game/matrices/task_1.png' }}"/>
    #https://yandex.ru/images/search?from=tabbar&text=%D1%84%D0%BE%D1%82%D0%BE%20%D0%BA%D0%BE%D1%82%D0%B0&pos=0&img_url=http%3A%2F%2Fwp-s.ru%2Fwallpapers%2F5%2F19%2F376948382466555%2Fpolosatyj-kot-s-zel-nymi-glazami-na-skame.jpg&rpt=simage&lr=213

    # test1 = models.IntegerField(
    #     label='''
    #     Сколько единиц в этой матрице?'''
    # )







    # task0 = models.IntegerField(
    #     label='''
    #      <br>
    #      <br>
    #      <br>
    #      <br>
    #      <br>
    #      <br>
    #      <br>
    #      <br>
    #      <br>
    #
    #     '''
    # )


    task1 = models.IntegerField(
        label=''' 
    Матрица 1. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task2 = models.IntegerField(
        label=''' 
    Матрица 2. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task3 = models.IntegerField(
        label=''' 
    Матрица 3. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task4 = models.IntegerField(
        label=''' 
    Матрица 4. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task5 = models.IntegerField(
        label=''' 
    Матрица 5. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task6 = models.IntegerField(
        label=''' 
    Матрица 6. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task7 = models.IntegerField(
        label=''' 
    Матрица 7. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task8 = models.IntegerField(
        label=''' 
    Матрица 8. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task9 = models.IntegerField(
        label=''' 
    Матрица 9. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task10 = models.IntegerField(
        label=''' 
    Матрица 10. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task11 = models.IntegerField(
        label=''' 
    Матрица 11. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task12 = models.IntegerField(
        label=''' 
    Матрица 12. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task13 = models.IntegerField(
        label=''' 
    Матрица 13. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task14 = models.IntegerField(
        label=''' 
    Матрица 14. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task15 = models.IntegerField(
        label=''' 
    Матрица 15. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task16 = models.IntegerField(
        label=''' 
    Матрица 16. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task17 = models.IntegerField(
        label=''' 
    Матрица 17. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task18 = models.IntegerField(
        label=''' 
    Матрица 18. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task19 = models.IntegerField(
        label=''' 
    Матрица 19. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task20 = models.IntegerField(
        label=''' 
    Матрица 20. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task21 = models.IntegerField(
        label=''' 
    Матрица 21. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task22 = models.IntegerField(
        label=''' 
    Матрица 22. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task23 = models.IntegerField(
        label=''' 
    Матрица 23. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task24 = models.IntegerField(
        label=''' 
    Матрица 24. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task25 = models.IntegerField(
        label=''' 
    Матрица 25. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task26 = models.IntegerField(
        label=''' 
    Матрица 26. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task27 = models.IntegerField(
        label=''' 
    Матрица 27. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task28 = models.IntegerField(
        label=''' 
    Матрица 28. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task29 = models.IntegerField(
        label=''' 
    Матрица 29. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task30 = models.IntegerField(
        label=''' 
    Матрица 30. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task31 = models.IntegerField(
        label=''' 
    Матрица 31. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task32 = models.IntegerField(
        label=''' 
    Матрица 32. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task33 = models.IntegerField(
        label=''' 
    Матрица 33. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task34 = models.IntegerField(
        label=''' 
    Матрица 34. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task35 = models.IntegerField(
        label=''' 
    Матрица 35. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task36 = models.IntegerField(
        label=''' 
    Матрица 36. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task37 = models.IntegerField(
        label=''' 
    Матрица 37. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task38 = models.IntegerField(
        label=''' 
    Матрица 38. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task39 = models.IntegerField(
        label=''' 
    Матрица 39. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task40 = models.IntegerField(
        label=''' 
    Матрица 40. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task41 = models.IntegerField(
        label=''' 
    Матрица 41. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task42 = models.IntegerField(
        label=''' 
    Матрица 42. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task43 = models.IntegerField(
        label=''' 
    Матрица 43. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
     '''
    )

    task44 = models.IntegerField(
        label=''' 
    Матрица 44. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task45 = models.IntegerField(
        label=''' 
    Матрица 45. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task46 = models.IntegerField(
        label=''' 
    Матрица 46. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task47 = models.IntegerField(
        label=''' 
    Матрица 47. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task48 = models.IntegerField(
        label=''' 
    Матрица 48. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task49 = models.IntegerField(
        label=''' 
    Матрица 49. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
     '''
    )

    task50 = models.IntegerField(
        label=''' 
    Матрица 50. <br> 
    Сколько единиц в этой матрице? <br> 
    &nbsp <br> 
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0<br>
    0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0<br>
    1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 0 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1 &nbsp&nbsp&nbsp 1<br>
     '''
    )


# FUNCTIONS

def set_scores(group: Group):
    Player1 = group.get_player_by_id(1)
    # Player.test_score = 0
    # p1 = group.get_player_by_id(1)
    # p2 = group.get_player_by_id(2)
    # p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
    # p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount

    player1_answers = [Player1.task1, Player1.task2, Player1.task3, Player1.task4, Player1.task5, Player1.task6,
                             Player1.task7, Player1.task8,
                             Player1.task9, Player1.task10, Player1.task11, Player1.task12, Player1.task13, Player1.task14,
                             Player1.task15, Player1.task16,
                             Player1.task17, Player1.task18, Player1.task19, Player1.task20, Player1.task21, Player1.task22,
                             Player1.task23, Player1.task24, Player1.task25,
                             Player1.task26, Player1.task27, Player1.task28, Player1.task29, Player1.task30, Player1.task31,
                             Player1.task32, Player1.task33, Player1.task34,
                             Player1.task35, Player1.task36, Player1.task37, Player1.task38, Player1.task39, Player1.task40,
                             Player1.task41, Player1.task42, Player1.task43,
                             Player1.task44, Player1.task45, Player1.task46, Player1.task47, Player1.task48, Player1.task49,
                             Player1.task50
                              ]
    for i in range(50):
        if player1_answers[i] == C.test_answers[i]:
            Player1.test_score += 1
        else:
            pass
    group.endowment = cu(Player1.test_score)


def sent_back_amount_choices(group: Group):
    return currency_range(0, group.sent_amount * C.MULTIPLIER, 1)


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = group.endowment - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount




def creating_session(subsession):
    for group in subsession.get_groups():
        if group.id_in_subsession % 2 == 0:
            group.treatment = "T"
        else:
            group.treatment = "NT"

def sent_amount_max(group):
    return group.endowment

def sent_back_amount_max(group):
    return group.sent_amount * C.MULTIPLIER

def expectations_player1_max(group):
    return group.sent_amount * C.MULTIPLIER


# PAGES
class Welcome(Page):
    after_all_players_arrive = creating_session
    form_model = 'group'



class Test(Page):
    timeout_seconds = 60*1 #60*15
    form_model = 'player'
    form_fields = ['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7', 'task8',
                   'task9', 'task10', 'task11', 'task12', 'task13', 'task14', 'task15', 'task16',
                   'task17', 'task18', 'task19', 'task20', 'task21', 'task22', 'task23', 'task24', 'task25',
                   'task26', 'task27', 'task28', 'task29', 'task30', 'task31', 'task32', 'task33', 'task34',
                   'task35', 'task36', 'task37', 'task38', 'task39', 'task40', 'task41', 'task42', 'task43',
                   'task44', 'task45', 'task46', 'task47', 'task48', 'task49', 'task50']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender', 'age']

class CognitiveReflectionTest(Page):
    form_model = 'player'
    form_fields = []

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

class ResultsWaitPage1(WaitPage):
    after_all_players_arrive = set_scores

class ResultsWaitPage4(WaitPage):
    after_all_players_arrive = sent_amount_max


class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(a = group.endowment * 1)


class WaitForP1(WaitPage):
    pass

class ResultsWaitPage3(WaitPage):
    after_all_players_arrive = sent_back_amount_max

class ResultsWaitPage5(WaitPage):
    after_all_players_arrive = expectations_player1_max


class After_Send(Page):
    form_model = 'group'
    form_fields = ['expectations_player1']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


class After_SendBack_NT(Page):
    form_model = 'player'
    form_fields = ['expectations_p1_player2', 'expectations_p2_player2']

    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return (player.id_in_group == 2 and group.treatment == 'NT')


class After_SendBack_T(Page):
    form_model = 'player'
    form_fields = ['expectations_p2_player2']

    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return (player.id_in_group == 2 and group.treatment == 'T')




class ResultsWaitPage2(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass



page_sequence = [Welcome, Test, CognitiveReflectionTest, ResultsWaitPage1, ResultsWaitPage4,
                 Demographics, Send, ResultsWaitPage3, ResultsWaitPage5, After_Send, WaitForP1, SendBack, After_SendBack_NT, After_SendBack_T, ResultsWaitPage2, Results]
