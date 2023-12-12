﻿image scenePr = "images/prequel1.png"
image sceneTime0 = "images/time0.png"
image sceneTime1 = "images/time1.png"
image sceneTime2 = "images/time2.png"
image sceneRoom = "images/room.png"
image sceneEnterCorp= "images/outside.png"
image sceneRyanRef = "images/ryanref2.png"
image sceneHall = "images/hall.png"
image sceneAdminTalk = "images/administration.png"
image sceneHrDoor = "images/hrdoor.png"
image sceneHrCab = "images/hrcab.png"
image sceneOffice = "images/office.png"
image sceneChoice1 = "images/office.png"
image scenePhone = "images/phone.png"
image sceneTitle = "images/title.png"
image shade = "images/dark.png"
image scenePartTime = "images/parttime.png"
image code1 = "images/code1.png"
image code2 = "images/code2.png"
image code3 = "images/code3.png"
image code4 = "images/code4.png"
image code5 = "images/code5.png"



image sceneTeam = "images/team.png"
image sceneTeamLead = "images/lead.png"
image sceneTeamDis = "images/dis.png"
image sceneTeamAnalyz = "images/analyz.png"
image sceneTeamDev = "images/dev.png"
image sceneTeamGamed = "images/gamedev.png"

image res11 = "images/job1.1.png"
image res12 = "images/job1.2.png"
image res13 = "images/job1.3.png"

define mainchar = Character('Артём', color="#017d0e")
define phone = Character('Мобильник',color = "#b4b0b0")
define hrbob = Character('Кошак',color = "#5a60cb")
define admin = Character('Администратор',color = "#2d34ff")
define teamlid = Character('Кирилл', color = "#f94848")
define alice = Character('Lариса',color = "#d12bab")
define n = Character(None, kind=nvl)

define audio.ringthone = "audio/wakeTheme.mp3"
define audio.office = "audio/partiaTheme.mp3"
define audio.room = "audio/roomTheme.mp3"
define audio.main = "audio/cosmoTheme.mp3"

define rate = 0
#image img = "images/*"

init:
    $ left = Position(xalign = 0.2, yalign = 1.1)
    $ right = Position(xalign = 0.8, yalign = 1.1)
    $ centre = Position(xalign = 0.6, yalign = 0.5)
    $ office = Position(xalign = 0.0, yalign = 1.1)
    $ score = 0

screen choice1():
    frame:
        background "shade"
        imagebutton:
            xalign 0.5
            yalign 0.3
            hover "images/header1.1.png"
            idle "images/hoverHeader1.1.png"
            action Return("+")
        imagebutton:
            xalign 0.5
            yalign 0.6
            hover "images/header1.2.png"
            idle "images/hoverHeader1.2.png"
            action Return("-")

screen choice2:
    frame:
        background "shade"
        imagebutton:
            xalign 0.1
            yalign 0.3
            hover "images/main1.1.png"
            idle "images/hoverMain1.1.png"
            action Return("+")
        imagebutton:
            xalign 0.85
            yalign 0.3
            hover "images/main1.2.png"
            idle "images/hoverMain1.2.png"
            action Return("-")

screen choice3:
    frame:
        background "shade"
        imagebutton:
            xalign 0.5
            yalign 0.3
            hover "images/footer1.1.png"
            idle "images/hoverFooter1.1.png"
            action Return("+")
        imagebutton:
            xalign 0.5
            yalign 0.6
            hover "images/footer1.2.png"
            idle "images/hoverFooter1.2.png"
            action Return("-")

screen choiceCode1():
    frame:
        background "code1"
        imagebutton:
            xalign 0.05
            yalign 0.85
            idle "images/code1.1.png"
            action Return("+")
        imagebutton:
            xalign 0.95
            yalign 0.85
            idle "images/code1.2.png"
            action Return("-")
screen choiceCode2():
    frame:
        background "code2"
        imagebutton:
            xalign 0.05
            yalign 0.85
            idle "images/code2.1.png"
            action Return("-")
        imagebutton:
            xalign 0.95
            yalign 0.85
            idle "images/code2.2.png"
            action Return("+")
screen choiceCode3():
    frame:
        background "code3"
        imagebutton:
            xalign 0.05
            yalign 0.95
            idle "images/code3.1.png"
            action Return("+")
        imagebutton:
            xalign 0.95
            yalign 0.95
            idle "images/code3.2.png"
            action Return("+")
screen choiceCode4():
    frame:
        background "code4"
        imagebutton:
            xalign 0.05
            yalign 0.85
            idle "images/code4.1.png"
            action Return("-")
        imagebutton:
            xalign 0.95
            yalign 0.85
            idle "images/code4.2.png"
            action Return("+")
screen choiceCode5():
    frame:
        background "code5"
        imagebutton:
            xalign 0.05
            yalign 0.85
            idle "images/code5.1.png"
            action Return("+")
        imagebutton:
            xalign 0.95
            yalign 0.85
            idle "images/code5.2.png"
            action Return("-")
label start:
    #play music cosmo
    window hide
    
    scene scenePr with dissolve    
    scene sceneTitle with fade
    $ renpy.pause(1.0)
    scene scenePr with fade

    n'''{cps=30}Артем Леонидович родился и провёл всё своё детство в городе Сургут.'''
    
    n'''{cps=30}Будучи в 8-ом классе, он начал увлекаться информатикой и программированием.'''
    
    n'''{cps=30}Принимал активное участие в научных конференциях и олимпиадах по программированию, что позволило ему получить дополнительные знания и навыки.\n'''
    
    n'''{cps=30}Окончив школу, Артём решил поступить в один из лучших университетов страны, УрФУ на 09 направление.'''
    nvl clear
    

    n'''{cps=30}В процессе обучения Артем решил, что после окончания вуза хочет стать фронтендером в IT-индустрии.'''
    
    n'''{cps=30}Он закончил УрФУ с отличием и получил степень бакалавра по специальности 'Программная инженерия'.'''
    
    n'''{cps=30}Артем понимал, для того чтобы найти работу в этой специальности, ему необходимо получить опыт работы.'''

    n'''{cps=30}Поэтому он начал искать вакансии на сайтах различных российских it-компаний.'''
    
    n'''{cps=30}Вскоре он нашел несколько интересных предложений от контор, которые предлагали стажировки.'''

    n'''{cps=30}Артём выбрал одну из таких вакансий и отправил свое резюме в компанию Headphones corp.'''
    nvl clear
    stop music
    scene sceneTime0 with fade
    n'''\n'''

    nvl clear
    
    scene sceneRoom with fade
    n'''\n'''
    nvl clear

    play music ringthone

    phone "{cps=10} Играет, что то знакомое, но это просто будильник..."

    stop music
    play music room

    show artem at left
    with dissolve
    show alice at right
    with easeinright
    
    menu:
        alice "{cps=30}Доброе утро, Артем! Рада видеть вас. Как ваше настроение?"
        "{cps=30}Доброе утро, Лариса. Настроение хорошее. Напомни ка мне, какие у меня сегодня планы?":
            call firstMorning from _call_firstMorning
        "{cps=30}Утро доброе. Настроение боевое, я сегодня выспался! Расскажи мне что-нибудь.":
            call secondMorning from _call_secondMorning
        "{cps=30}Такое себе доброе утро. Я вообще не выспался.":
            call thirdMorning from _call_thirdMorning
    
    hide alice with easeoutright
    window hide
    n'''\n'''
    stop music
    
    scene sceneTime1 with fade
    n'''\n'''

    scene sceneRoom with fade

    play music room

    show artem
    mainchar "{cps=30}Ухх, какая тренировка была. А как я покушал после этой тренировки, ммм..."
    hide artem

    scene scenePhone with fade

    play music ringthone
    with Pause(0.5)

    phone "{cps=10}Бз-бз-бз-бз..."
    
    stop music
    play music room

    scene sceneRoom with fade
    show artem at left

    mainchar "{cps=30}Здравствуйте, кто это?"
    "{cps=30}..." "{cps=30}Здравствуйте, меня зовут Роберт Кошак и я являюсь представителем компании Headphones corp." 
    hrbob "{cps=30}Вы недавно отправляли свое резюме на нашу корпоративную почту, и наша компания готова рассмотреть вашу кандидатуру. 
            Приглашаем вас на собеседование/стажировку, которое будет в четверг в 9 часов утра"
    mainchar "{cps=30}Спасибо, до свидания!"

    hide artem with dissolve

    window hide
    n'''\n'''

    stop music
    
    scene sceneTime2 with fade
    n'''\n'''

    scene sceneEnterCorp with fade
    n'''\n'''

    scene sceneRyanRef with fade
    n'''\n'''
    mainchar "{cps=30}..."
    play music office

    scene sceneAdminTalk with fade
    
    show artem at right

    mainchar "{cps=30}Администратор?"
    admin "{cps=30}Здравствуйте, чем могу быть полезен?"
    mainchar "{cps=30}Здравствуйте, меня пригласили на собеседование."
    admin "{cps=30}Супер, поздравляю вас! Не могли бы вы мне сказать время, на которое у вас стоит собеседование?"
    mainchar "{cps=30}У меня собеседование стоит на 9:00."
    admin "{cps=30}Ага, вижу вас по базе. Ваше имя Артем Леонидович?"
    mainchar "{cps=30}Да, это я."
    admin "{cps=30}Хорошо. Вам нужно будет пройти в кабинет нашего менеджера. Он находится на 2 этаже."
    mainchar "Спасибо."

    scene sceneHrDoor with fade
    "{cps=10}Тук-тук-тук"

    scene sceneHrCab with fade
    show bob at right
    hrbob "{cps=30}Здравствуйте! Вы знаете - меня зовут Роберт Кошак. Расскажите мне немного о себе."
    show artem at left
    mainchar "{cps=30}Здравствуйте, я закончил университет по специальности 'программная инженерия' с красным дипломом. Хочу работать в большой международной компании."
    hrbob "{cps=30}Нам нужен человек, который будет заниматься версткой веб-приложений. Что вы знаете про верстку?"
    mainchar "Я умею делать лэндинги на html+css+js, также могу работать с бэкэндом на Python и PHP"
    hrbob "{cps=30}Это хорошо! Вы уже работали с какой-либо системой управления проектами?"
    mainchar "{cps=30}Да, я работал с Jira."
    hrbob "{cps=30}Итак я думаю этого достаточно, вы приняты на испытательный срок!"
    mainchar "{cps=30}Спасибо."
    hrbob "{cps=30}Ждём вас завтра"

    hide bob

    hide artem
    stop music
    scene sceneRoom with fade

    show artem at left

    mainchar "{cps=30}Интересно, что ждёт меня на новой работе!"

    hide artem


    scene sceneOffice with fade
    play music office
    mainchar "{cps=30}Вот моё рабочее место"

    show kiril at office

    teamlid "{cps=30}Здравствуйте, Артём! Меня зовут Кирилл Владиславович. "
    teamlid "{cps=30}Мне Роберт Кошак позвонил и сказал, что отправил вас на испытательный срок."

    menu:
        teamlid "{cps=30}Вы, наверное, уже догадались, что вы будете за мной закреплены."
        "Здравствуйте! Да, я уже это понял.":
            call nothing from _call_nothing
        "Здравствуйте, Кирилл Владиславович! Рад знакомству!":
            call nothing from _call_nothing_1
    menu:
        teamlid "{cps=30}Хотите я немного расскажу о вашей должности? Или же вы сразу приступите к первому заданию?"    
        "Давайте я лучше сразу приступлю к работе, хорошо?":
            call nothing from _call_nothing_2
        "Не откажусь! Это будет интересно. ":
            call about from _call_about
        

    teamlid "{cps=30}Твое первое задание объединить макеты в лэндинг. Результат отправишь мне."
    teamlid "{cps=30}Дизайнер отошлет тебе варианты, разберёшься"

    hide kiril with easeinleft

    $ finalResult = 0;
    "{cps=30}Вот наброски, но начни верстать сейчас,тк очень нужна страничка для донорского центра 'красное/белое'"

    $ result = renpy.call_screen("choice1")    
    
    if result == "+":
        $ score = score + 1
    else:
        $ score = score - 1

    $ result = renpy.call_screen("choice2")
    if result == "+":
        $ score = score + 1
    else:
        $ score = score - 1

    $ result = renpy.call_screen("choice3")
    if result == "+":
        $ score = score + 1
    else:
        $ score = score - 1
    
    if score == 3:
        $ finalResult = finalResult + 1;
        mainchar "{cps=30}Сообщение: Получилось как-то так..."
        window hide
        scene res11 with fade
        n'''\n'''
        scene office with fade

        teamlid "{cps=30}Ответ: Вот, так. Этот искиз идеально подходит под тематику сайта. Отлично!"

    if score == -3:
        $ finalResult = finalResult + 1;
        mainchar "{cps=30}Сообщение: Получилось как-то так..."
        window hide
        scene res12 with fade
        n'''\n'''
        scene office with fade
        teamlid "{cps=30}Ответ: Так, выглядит интересно, хмммм.... ну ладно, этот эскиз мне нравиться!"

    if score != -3 and score != 3:
        $ finalResult = finalResult + 1;
        mainchar "{cps=30}Сообщение: Получилось как-то так..."
        window hide
        scene res13 with fade
        n'''\n'''
        scene office with fade
        teamlid "{cps=30}Ответ: Ну нет, такой эскиз не годиться!"

    window hide
    scene scenePartTime with fade
    n'''\n'''

    scene sceneOffice with fade
    show kiril at office
    teamlid "{cps=30}Снова здравствуй."
    mainchar "{cps=30}Здравствуйте."
    teamlid "{cps=30}Так, вот и следующее задание. Я даю тебе 5 кодов, а ты должен написать в документацию, что он будет выводить или делать. Все просто не так-ли?"
    mainchar "{cps=30}Хорошо"
    hide kiril
    window hide
    $ result = renpy.call_screen("choiceCode1")
    if result == "+":
        $ finalResult = finalResult + 1
    $ result = renpy.call_screen("choiceCode2")
    if result == "+":
        $ finalResult = finalResult + 1
    $ result = renpy.call_screen("choiceCode3")
    
    $ result = renpy.call_screen("choiceCode4")
    if result == "+":
        $ finalResult = finalResult + 1
    $ result = renpy.call_screen("choiceCode5")
    if result == "+":
        $ finalResult = finalResult + 1
    window hide
    scene scenePartTime with fade
    n'''\n'''
    scene sceneOffice with fade
    show kiril at office
    teamlid "{cps=30}Итак посмотрим каковы твои результаты за испытательный срок"
    teamlid "{cps=30}Мгм [finalResult] по пятибальной шкале"
    if finalResult == 5:
        teamlid "{cps=30}Поздравляю вас примут на основную должность!"
        jump goodEnding
    if finalResult == 4:
        teamlid "{cps=30}Я думаю, что вы заслуживаете место в нашей компании..."
        jump goodEnding
    if finalResult == 3:
        teamlid "{cps=30}А могли ж ведь лучше! К сожалению. Мы не можем принять вас в нашу компанию."
        jump badEnding
    if finalResult == 2 or finalResult == 1 or finalResult == 0:
        teamlid "{cps=30}К сожалению. Мы не можем принять вас в нашу компанию."
        jump badEnding   
    return

label goodEnding:
    teamlid "{cps=30}Зайдите позже в кабинет Роберта Кошака. Я ему скинул отчет по проделанной работе. "
    mainchar "{cps=30}Хорошо. До свидания."
    teamlid "{cps=30}Всего доброго. И добро пожаловать в нашу компанию!"
    hide teamlid with easeinleft
    mainchar "{cps=30}Аллилуя!"

    scene sceneHrCab with fade
    show bob at right
    show artem at left
    hrbob "{cps=30}Здравствуйте, Артем! Я получил отчет о проделанной вами работе." 
    hrbob "{cps=30}Штош.... Я могу вас только поздравить с получением рабочего места в нашей компании! "
    hrbob "{cps=30}Работать приступаете в понедельник. Ждем вас как всегда в 9 утра."
    mainchar "{cps=30}Я так рад этому событию. Спасибо вам огромное! До свиданья!"
    hrbob "{cps=30}До свиданья."
    hide bob
    hide artem
    
    scene sceneRyanRef with fade
    "{cps=30}Видимо это конец, штош хорошо то что хорошо кончается..."
    window hide
    n'''\n'''
    return

label badEnding:
    teamlid "{cps=30}Зайдите позже в кабинет Роберта Кошака. Я ему скинул отчет по проделанной работе. До свиданья..."
    hide teamlid with easeinleft
    mainchar "{cps=30}Неловко вышло."
    scene sceneHrCab with fade
    show bob at right
    show artem at left
    hrbob "{cps=30}Здравствуйте, Артем! Я получил отчет о проделанной вами работе." 
    hrbob "{cps=30}Штош...очень жаль что вы не оправдали наши ожидания, вы свободны. До свиданья."
    mainchar "{cps=30}До свиданья."
    scene sceneRyanRef with fade
    mainchar "{cps=30}Дурацкие Headphones..."
    "{cps=30}Эм, видимо The End."
    window hide
    n'''\n'''
    return

label firstMorning:
    alice "{cps=30}Напоминаю вам, что у вас запланировано несколько дел. Сначала у вас есть тренировка в 9:30 утра."
    alice "{cps=30}Затем вам стоит ожидать звонок от компании Headphones corp., звонить вам будут по поводу вашего отправленного резюме неделей ранее."
    alice "{cps=30}Звонок должен поступить после обеда. После этого у вас нет других запланированных дел."
    mainchar "{cps=30}О, спасибо. Пойду завтракать и побегу на тренировку."
    alice "{cps=30}Обращайтесь еще, всегда рада вас слышать!"
    return

label secondMorning:
    alice "{cps=30}Расскажу вам о сегодняшней погоде. Сегодня ожидается переменная облачность с периодами солнечной погоды."
    alice "{cps=30}Температура будет колебаться от +18 до +23 градусов Цельсия. Ветер будет слабый, юго-западный."
    alice "{cps=30}Что-нибудь еще? Например, я могу рассказать про ваши планы на сегодняшний день."
    mainchar "{cps=30}Давай!"
    
    alice "{cps=30}Напоминаю вам, что у вас запланировано несколько дел. Сначала у вас есть тренировка в 9:30 утра."
    alice "{cps=30}Затем вам стоит ожидать звонок от компании Headphones corp., звонить вам будут по поводу вашего отправленного резюме неделей ранее."
    alice "{cps=30}Звонок должен поступить после обеда. После этого у вас нет других запланированных дел."
    mainchar "{cps=30}Вот блин, забыл совсем про тренировку....пойду завтракать и собираться. Спасибо что напомнила."
    alice "{cps=30}Всегда пожалуйста!"
    return

label thirdMorning:
    alice "{cps=30}Артем, а вы знали, что если человек не высыпается, это может привести к ряду негативных последствий для его здоровья и благополучия?"
    mainchar "{cps=30}Да знаю я это все. Я веселиться хочу, лето же еще на дворе."
    alice "{cps=30}Кроме того, недостаток сна может снизить иммунитет, повысить уровень стресса и ухудшить память и концентрацию."
    mainchar "{cps=30}Да ну тебя....нудная ты. Лучше расскажи мне, какие у меня сегодня дела."

    alice "{cps=30}Напоминаю вам, что у вас запланировано несколько дел. Сначала у вас есть тренировка в 9:30 утра."
    alice "{cps=30}Затем вам стоит ожидать звонок от компании Headphones corp..."
    mainchar "{cps=30}Мгхм...так никуда не хочется идти. А когда мне должны будут позвонить?"
    alice "{cps=30}Звонок должен потупить после полудня."
    mainchar "{cps=30}Спасибо, что напомнила. Я пошел собираться на тренировку."
    alice "{cps=30}Всегда рада вам помочь! Обращайтесь!"
    return

label about:
    teamlid "{cps=30}Frontend’er взаимодействует с дизайнерами, обсуждает концепции и детали интерфейса."
    teamlid "{cps=30}Он воплощает их идеи в код, вдыхая жизнь в каждый пиксель."
    teamlid "{cps=30}HTML, CSS, JavaScript — это его инструменты, кисти, которыми он создает виртуальные шедевры."
    teamlid "{cps=30}Постоянный поиск совершенства становится его привычкой. Он тестирует и оптимизирует свои творения, чтобы они выглядели и работали идеально на всех устройствах и во всех браузерах."
    teamlid "{cps=30}Разработчик становится архитектором интерфейса, строя крепкий фундамент для комфортного взаимодействия пользователя с веб-приложением."
    teamlid "{cps=30}Frontend’er не просто создает красивые страницы — он делает их интуитивно понятными и удобными."
    teamlid "{cps=30}Он обеспечивает отзывчивость и быстродействие, чтобы пользователь мог наслаждаться плавным и приятным опытом взаимодействия с сайтом."
    teamlid "{cps=30}Часы летят незаметно, когда Frontend’er увлечен своей работой. Он решает технические задачи, ищет новые технологии и подходы, чтобы быть впереди времени."
    teamlid "{cps=30}Иногда ему приходится сталкиваться с багами и трудными моментами, но именно они делают его сильнее и опытнее."
    teamlid "{cps=30}Когда работа заканчивается, фронтендер несет свой вклад в виртуальный мир, делая его красивее и функциональнее. Его труд виден в каждом щелчке мыши, в каждом взгляде пользователя на интерфейс."
    teamlid "{cps=30}И, несмотря на то, что его труд невидим для обычного пользователя, фронтендер знает, что его работа создает тот невероятный опыт, который сделает визит пользователя на сайт незабвенным."
    teamlid "{cps=30}Ну вот как-то так. Пока что вы будете выполнять мои относительно простые знатия."


label nothing:
    return