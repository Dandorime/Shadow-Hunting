label learn_about_conflicts: 

    li "Проблемы в коллективе?"

    "Я не смогла сдержать любопытства.{w} Профессор вздохнул{w} и начал протирать свои очки о рубашку."

    bar "Видите ли,{w} мисс Донован{w}, один из ваших коллег недоволен работой в лаборатории.{w} Он настоятельно просил меня усилить контроль за лаборантами."

    '''
    Мистер Барни вновь устало вздохнул. 
    
    По опыту прошлых лет, я знала, что профессор совсем не любил бумажную работу. Он был фанатом своего предмета и любил вести лекции. 
    
    Было неудивительно, что перспектива вести излишнюю документацию и следить за работой лаборантов его не очень-то и радовала.
    '''

    bar "Понимаете, мисс Донован, я уверен, что вы и ваши коллеги уже взрослые люди, и я не вижу смысла просить вас отчитываться за каждый шаг.{w} По себе знаю, что это очень мешает работе."

    "Мне оставалось лишь только кивать."

    bar "Я надеюсь, что вам удасться решить все разногласия без участия ректората. Так ведь всем будет проще."

    "Он взглянул на наручные часы."

    bar "Извините, мне пора спешить на первую пару.{w} Не забудьте про доставку веществ{w}, хорошо?"

    li "Конечно. До свидания."

    hide bar_img
    with dissolve

    "Он исчез так же быстро, как и подошел ко мне. Но я была только рада{w} – не знаю, что я должна была сказать ему в ответ."

    '''
    Подобно профессору, я посмотрела на часы в холле и поспешила в сторону лаборатории.

    По дороге в лабораторию я невольно прокручивала разговор с мистером Барни в голове.

    Кто из коллег мог пожаловаться? И главное — на что? 
     
    Конечно, у нас у всех бывали недопонимания, но до этого никто не высказывал серьезных претензий.

    Я вздохнула, еще крепче сжав ремешок сумки. Пока не было смысла строить догадки. Нужно было дождаться доставки реактивов и просто присмотреться к коллегам. Возможно, ответ найдется сам собой.
    '''
    
    jump turned_left

    return

label turned_left:

    show bg wardrobe
    with dissolve

    '''
    Я свернула налево к лабораторному блоку. На полпути услышала знакомый звук — скрип двери в конце коридора. Кто-то уже был в лаборатории.
    
    Возле шкафчиков в раздевалке стоял уже знакомый силуэт: коричневый свитер, джинсы и взлохмаченные волосы – это был Алекс.
    '''

    hide lina pajamas
    with dissolve

    show al casual 
    with dissolve

    '''
    С Александром я познакомилась еще будучи подростком: вместе мы ходили в одну школу и пересекались на перерывах, хоть он и был старше меня на год.
    
    В старших классах друзей кроме Алекса у меня особо не было. Ребенком я была скорее застенчивым и интровертным, чего нельзя было сказать о нем.
    
    Теперь дружелюбный Александр возглавлял наш небольшой коллектив лаборатории.
    '''

    hide al casual
    with dissolve

    show lina casual at left2
    with dissolve

    show al casual at right2
    with dissolve

    "Обычно спокойный и дружелюбный парень сейчас задумчиво и немного хмуро рылся в своем шкафчике.{w} Я подошла к нему со спины."

    li "Хэй"

    "Я поздоровалась, и он дернулся от неожиданности, а после развернулся ко мне"

    al "Черт{w}, напугала.{w} Привет.{w} Ты сегодня рано."

    li "Барни сказал, что сегодня доставка реактивов. Подумала, нужно расчистить место"

    "Я говорила, пока снимала пальто и убирала лишние вещи в шкафчик. Алекс задумчиво наблюдал за мной, тихо кивая."

    al "Да, я помню. Их должно быть немного, одна-две коробки."

    "Пока я надевала белый халат, Алекс нервно и задумчиво теребил края своего свитера. Собираться в полной тишине было даже странно – обычно я всегда слушала его болтовню."

    hide lina casual

    show lina robe at left2
    with dissolve

    li "Ты чего такой тихий?{w} Не выспался?"

    "Он снова дернулся, будто мои слова выдернули его из мыслей.{w} Алекс слегка усмехнулся."

    al "Да так, просто торможу сегодня.{w} Плохо спал."

    "Он замолчал, но заговорил после короткой паузы."

    al "Ты иди, я скоро буду.{w} Там…{w} уже Джон на месте."

    '''
    Я слегка растерянно кивнула и пошла в лабораторию, захватив очки из сумки. 
    '''

    hide al casual
    with dissolve

    '''
    
    Я решила, что не стоит доставать Алекса с утра: в конце концов, я знаю, как много он работает.
    
    Хотя многие и называют нашу лабораторию унылым местом, мне здесь нравится. Среди тусклых серых стен, столов и колб я ощущаю спокойствие. 
    
    Я знаю, что буду делать каждый день, с какими веществами и людьми я буду работать.
    
    Когда я зашла в комнату, меня встретила привычная обстановка. Столы, шкафы с колбами, все как всегда стояло на своих местах.
    
    Это постоянство добавляло в мои будни то спокойствие, которого иногда не хватало.
    
    В комнате слышался тихий шум воды. Я повернула голову к источнику звука – один из моих коллег мыл колбы у раковины. 
    
    Он стоял спиной ко мне, и я не сразу поняла, кто это был.
    '''

    li "Привет"

    "Парень повернул голову и выключил воду. Он вытер колбу полотенцем и развернулся ко мне."

    hide lina robe

    show john robe
    with dissolve

    john "А, это ты.{w} Привет."

    '''
    По недовольному голосу и блестящим туфлям я сразу поняла, что передо мной стоял Джон.
    
    Джон, как и я, был младшим сотрудником лаборатории.
    
    Высокий, худощавый, с идеально уложенными светло-русыми волосами и неизменно безупречным стилем. 
    
    Джон всегда выглядел так, будто только что сошел с обложки модного журнала.
    
    Идеально выглаженный белый халат, аккуратно застегнутые пуговицы на рубашке и, конечно же, эти сверкающие туфли, которые, кажется, никогда не знали грязи или пятен.
    
    Джон познакомился с Алексом год назад и стал его негласным протеже: именно Александр помогал ему заданиями, а после взял работать в лабораторию.
    
    Я не знала, в чем было дело, но сейчас их отношения были весьма напряженно. Нередко я становилась свидетелем их колких разговоров во время рабочей смены.
    
    Казалось, временами они просто раздражали друг друга из-за разных взглядов на работу.
    
    Джон выжидающе смотрел на меня, скрестив руки на груди. Я неловко прокашлялась.
    '''

    hide john robe
    show lina robe at left2 
    with dissolve
    show john robe at right2 
    with dissolve

    li "Как дела?"

    john "Ничего нового. Домываю за вами колбы{w}, как всегда."

    "Я поджала губы. Джону была важна идеальная чистота, мне было достаточно отсутствие полного бардака, а Алекса редко заботили такие детали."

    li "Барни сказал, что сегодня привезут реактивы…"

    john "Поэтому я решил расчистить место."

    '''
    Джона нельзя было назвать дружелюбным, но сегодня, по его голосу, он показался мне особенно недовольным.
    
    Алекс тоже показался мне странным сегодня.
    
    С Джоном мы не были близкими друзьями, но я все равно могла бы попытаться узнать, что случилось. Хотя, может, стоило бы подготовиться к работе.
    '''

    show bg laboratory
    with dissolve
    
    menu:
        "Что делать?"

        "Узнать у Джона, случилось ли что-то":
            jump ask_john

        "Подготовиться к работе":
            jump ready_for_work

    return

label ask_john:

    li "Все нормально?"
    
    "Я старалась задать вопрос так деликатно, как только могла. Однако Джон все равно демонстративно фыркнул, не скрывая своей реакции."

    john "Ну если ты считаешь, что использовать лабораторию вуза в своих целях – это нормально, то тогда проблем нет."

    '''
    Ну конечно. Мне стоило догадаться, почему Джон снова был недоволен.
    
    Эта история длилась уже около месяца. Алекс, известный трудоголик, часто брал сверхурочные заказы от разных предприятий. 
    
    И так как отдельно искать помещение было слишком дорого, он часто задерживался допоздна в нашей лаборатории.
    
    Так как он возглавлял наш отдел, а со стороны администрации почти не было контроля, Александр легко выполнял свои заказы в нерабочее время.
    
    Конечно, на самом деле это было не совсем легально. Я мало что понимаю в праве, но все это выглядело, как превышение должностных полномочий. 
    
    И все равно для меня это не было такой большой проблемой, как для Джона.
    
    Узнав об этом, мой коллега и друг постоянно пытался поговорить с Алексом насчет этой ситуации.
    
    И хотя я все не понимала, почему Джонатан так беспокоится о нашей лаборатории, видимо, их разговоры с Алексом постепенно превратились в конфликты.
    '''

    li "Слушай, Алекс всего лишь зарабатывает для семьи деньги. Он очень порядочный, так что я не думаю, что универ терпит большие убытки из-за его…"
    
    john "Да дело даже не в этом!"
    
    "Джон резко начал говорить громче, но тут же успокоился, не желая устраивать сцену на рабочем месте. Он вздохнул и снял очки, протирая стекла халатом."
    
    john "Он постоянно приносит сюда свои образцы, использует оборудование для каких-то проектов. Иногда даже в рабочее время. Я просил его прекратить, но ему все равно на мои слова."
    
    "Он надел очки обратно и скрестил руки на груди."
    
    john "Я не хочу подставлять его, но и он не имеет права пользоваться ресурсами университета."

    '''
    Я задумчиво отвела взгляд в сторону. Конечно, отчасти Джон был прав, но мне мало верилось в его заботе о нашем вузе. 
    
    Но даже если его беспокоит что-то еще, он вряд ли расскажет мне все это сейчас, на взводе после неприятного разговора с Алексом.
    
    Я снова подняла глаза на Джонатана. Очевидно, он ждал от меня хоть какой-то реакции.
    '''

    menu:
        "Что делать?"

        "Поддержать Джона":
            jump support_john

        "Защитить Алекса":
            jump def_alex

    return

label ready_for_work:

    hide john robe
    with dissolve

    '''
    Я бросила взгляд на Джона, но он уже отвернулся, вернувшись к своим колбам. Может, и правда стоило просто заняться работой.
    
    Я подошла к своему рабочему столу. Пара колб все еще стояла на краю, за ними – стопка лабораторных журналов, а на подоконнике валялась забытая перчатка.
    
    Сначала я собрала разбросанные журналы и аккуратно сложила их в стопку. 
    
    Потом вытерла влажным полотенцем поверхность стола – липкое пятно возле держателя для пробирок заставило меня поморщиться.
    
    Похоже, кто-то вчера оставил что-то неубранным.
    
    Я взяла колбы и отнесла их к раковине. 
    Джон мельком взглянул на меня, но ничего не сказал.
    
    Я включила воду и осторожно начала мыть стекло, ощущая, как теплая вода согревает пальцы. Мыльная пена стекала в раковину, и я на мгновение позволила себе просто сосредоточиться на ощущении чистоты.
    
    Я закрыла воду и вытерла руки полотенцем. Уборка заняла всего несколько минут, но мысли в голове только усложнились. Может, стоило все-таки поговорить с Алексом. Или хотя бы проследить за ним.
    
    Я убрала полотенце на место и выпрямилась. Пора было приступать к работе.
    '''

    jump in_labo
    with dissolve

    return

label support_john: 

    '''
    Несмотря на всю свою привязанность к Алексу, его поступки становились всё более очевидными, и их было невозможно игнорировать.
    
    Я знала, что Джон прав. 
    
    Но как бы мне ни хотелось поддержать Алекса, я не могла отрицать очевидное — его действия были не совсем корректными.
    
    Я посмотрела на Джона. Его глаза горели решимостью, но это не был тот Джон, которого я привыкла видеть. 
    
    Этот человек был измотан, перегружен заботами и в какой-то степени разочарован.
    '''
    
    li "Наверное, ты прав. Мы все как-то слишком привыкли к его самовольству. Даже я."

    "Джон выглядел немного ошеломлённым. Возможно, он ожидал, что я буду оправдывать Алекса, как всегда. Я продолжила."

    li "Но мне бы не хотелось, чтобы это не перешло в серьезный конфликт. Я знаю, что ты прав, но давай попробуем найти другой способ решения проблемы."
    
    "Я могла чувствовать, как Джон начинает успокаиваться. Он не злился, но была видна напряжённость."


    li "Давай попробуем поговорить с ним вместе. Просто обсудим это спокойно. Если оба скажем, что ситуация выходит за рамки, может быть, он прислушается?"
    
    "Джон задумался. Было видно, что он сомневается, но в конце концов он кивнул."

    john "Ладно. Но только потому, что ты попросила."
    
    hide john robe
    with dissolve

    '''
    Я вздохнула с облегчением. Осталось только поговорить с Алексом, но я подумала, что сделать это лучше после смены или во время обеда. 
    
    Сейчас главное, чтобы они немного успокоились.
    
    Джон пошел к своему рабочему столу, больше не желая общаться.
    '''

    jump in_labo
    with dissolve

    return

label def_alex: 

    '''
    Я могла понять недовольство Джона. Конечно, в чем-то он был прав: Алексу действительно не стоило так часто пользоваться возможностями лаборатории. 
    
    Но я знала его уже не первый год и могла быть уверена, что в его действиях точно нет злого умысла.
    
    Я давно не интересовалась его делами и легко могла упустить проблемы в его жизни. Перед тем, как предъявлять ему претензии, стоило узнать о его ситуации побольше.
    
    И даже несмотря на то, что я могла понять Джона, мне нужно было найти веские причины для того, чтобы оправдать Алекса. 
    
    Он был человеком, который никогда не ставил себя на первое место, и его проблемы, как бы странно это ни звучало, всегда были связаны с его желанием помочь другим.
    
    Я почувствовала, как моё сердце начало колотиться, но я постаралась сохранить спокойствие, не позволяя себе поддаться давлению.
    '''

    li "Я понимаю, что ты злишься. Но мне кажется, у Алекса могут быть веские причины для того, чтобы нарушать правила."
    
    "Джон скептически вскинул бровь. Он явно был готов к очередному спору."
    
    li "Мы не можем точно знать, что у него на уме, но я уверена, что он бы не стал использовать лабораторию в своих целях просто так."
    
    "Джон напрягся еще сильнее. Он неподвижно смотрел на меня, будто пытаясь уловить хоть одну свободную секунду, чтобы возразить мне."
    
    li "Давай я поговорю с ним. Скажу, что его действия не совсем уместны и спрошу причину." 
    
    john "Ты его слишком оправдываешь. Мы на работе, а тут все должно быть четко."
    
    li "Я просто хочу понять, почему он так поступает. Я поговорю с ним и постараюсь выяснить всё спокойно."
    
    '''
    Джонатан молчал, повернувшись к столу и перебирая какие-то бумаги. 
    
    Его молчание говорило о том, что он не был до конца согласен, но по крайней мере он не продолжал спорить.
    
    В конце концов он уперся руками в стол и сквозь зубы сказал.
    '''

    john "Ладно."

    hide john robe
    with dissolve
    
    '''
    А после он быстро удалился к своему рабочему место, явно давая понять, что не намерен продолжать диалог.
    
    Зная характер Джона и его терпение, мне стоило поговорить с Алексом побыстрее. 
    
    Но я решила повременить хотя бы до конца рабочей смены. Кажется, нам всем стоит остыть.
    '''

    jump in_labo
    with dissolve

    return