#角色定义

define sd = Character("五河士道", 
    who_color="#c8c8ff",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#c8c8ff",2,0)],
    image="sd"
    )
define ql = Character("五河琴里", 
    who_color="#c8ffc8",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#c8ffc8",2,0)],
    image="ql"
    )
define ys = Character("月咲绫", 
    who_color="#ffc8c8",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffc8c8",2,0)]
    )
define hm = Character("殿町宏人", 
    who_color="#ffffc8",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffffc8",2,0)]
    )
define xz = Character("小珠老师", 
    who_color="#ffc8ff",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffc8ff",2,0)]
    )
define hz = Character("立花火织", 
    who_color="#ffc8ff",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffc8ff",2,0)]
    )
define ks = Character("时崎狂三", 
    who_color="#ffc8ff",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffc8ff",2,0)]
    )
define unknow = Character("???", 
    who_color="#ffffff",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffffff",2,0)]
    )
define girl = Character("少女", 
    who_color="#ffc8c8",
    #what_prefix="【",
    #what_suffix="】",
    who_outlines=[(1,"#ffc8c8",2,0)]
    )


image side ql="images/Avatar/Kotori Itsuka/ql_white.png"
image side ql w="images/Avatar/Kotori Itsuka/ql_white.png" #白琴里
image side ql b="images/Avatar/Kotori Itsuka/ql_black.png" #黑琴里

image side sd = "images/Avatar/Shidou Itsuka/shidou_itsuka.png"

image ql :
    xpos 1920
    ypos 1080
    xanchor 1.0
    yanchor 1.0
    zoom 0.7
    "images/Character Illustration/Kotori Itsuka/ql_white.png"

image ql b:
    xpos 1920
    ypos 1610
    xanchor 1.0
    yanchor 1.0
    zoom 0.6
    "images/Character Illustration/Kotori Itsuka/ql_black.png"

image ql w:
    xpos 1920
    ypos 1670
    xanchor 1.0
    yanchor 1.0
    zoom 1.1
    "images/Character Illustration/Kotori Itsuka/ql_white.png"

image sd:
    xpos 1920
    ypos 1800
    xanchor 0
    yanchor 1.0
    zoom 0.4
    "images/Character Illustration/Shidou Itsuka/shidou_itsuka1.png"

image sd zoom_x:
    xpos 600
    ypos 1800
    xanchor 0
    yanchor 1.0
    zoom 0.4
    xzoom -1
    "images/Character Illustration/Shidou Itsuka/shidou_itsuka1.png"

image ys :
    xpos 0
    ypos 1500
    xanchor 0.0
    yanchor 1.0
    zoom 0.4
    xzoom -1.0
    "images/Character Illustration/Tsukisaki Aya/月咲绫.png"

image ys right_:
    xpos 1920
    ypos 1500
    xanchor 1.0
    yanchor 1.0
    zoom 0.4
    "images/Character Illustration/Tsukisaki Aya/月咲绫.png"

image ys left_:
    xpos 0
    ypos 1500
    xanchor 0.0
    yanchor 1.0
    zoom 0.4
    xzoom -1.0
    "images/Character Illustration/Tsukisaki Aya/月咲绫.png"


#背景图定义
image background_start = "images/Background/start.png"
image background_sd_kt = "images/Background/sd_kt.jpeg"

label start:
    define a=0

    scene background_start

    "我叫五河士道，是一名平凡的高中生"

    "今天，我像往常一样买菜回来，发现一位少女倒在门前"

    show sd
    
    sd "(轻轻摇晃少女的身体)喂，没事吧？"

    "毫无反应"

    sd "看来是昏迷了，不能坐视不管"

    hide sd

    "于是我将那名少女抱回了屋里"

    scene background_sd_kt

    show sd

    sd "呼~，就先安置在沙发这里吧"

    hide sd

    "士道简单打量了一下"

    "这位少女有着黑色的秀发,身上的洋服是白色的,下半身则是穿着百褶裙"

    "现在躺在沙发上，简直就像一个精致的洋娃娃一样。"

    show sd 

    sd "(视线来到少女的手中)她手里貌似握着一个东西？"

    sd "算了，还是不要过多关注比较好"

    "士道提前倒好一杯水放在桌上，等待她醒来。"

    unknow "哥哥你回来了吗？什么时候做晚饭呢？这个女孩是谁呀？难道是新交的女朋友吗?"

    "寻声望去,是我的妹妹五河琴里"

    sd "不是的!这个女孩倒在了我们家门口，我总不能见死不救吧，饿了的话，我现在就做饭吧"


    "士道正准备去做饭时，沙发那边传来声响"

    hide sd 

    show sd
    
    with dissolve

    show ys

    "循声望去，少女正揉着眼睛缓慢起身，紧握的手也随之松开，手上的东西也随之掉在地上，是一把钥匙"

    sd "你醒了？(看向钥匙)这是？钥匙？"

    "将钥匙从地上捡了起来"

    "感觉这钥匙在哪里见过?"

    "还没等我细想，少女的声音便传了过来"

    girl "快还给我！！！"

    sd "啊，对不起，我马上给你"

    "接到钥匙的少女马上松了一口气"

    sd "话说你叫什么名字？来自哪里？"

    girl "我叫月咲绫，其他的...不记得了"

    "女孩冰冷的回答道，那声音不带任何感情，简直就像人偶一样。"

    "果然还是报警吧"
    show ql

    ql w "士道，把她留下来吧，月咲似乎失去了大部分的记忆，贸然报警可能会招来麻烦"

    "琴里突然改变了对我的称呼，头上的蝴蝶结也变成了黑色"

    sd "好吧"

    "..."

    "......"

    "经过我和琴里的协商，我们决定暂时将月咲小姐留下了，直到她恢复记忆为止"

    "途中我们也询问了一下月咲小姐的意见，她表示也没问题"

    sd "那行，你们应该都饿了吧，我先去给你们做饭了"

    "..."

    scene bg room #他人视角

    ql "#待补充。。。,为琴里向月咲打招呼的对话"

    ys "..."

    scene background_sd_kt

    show ql

    sd "好了，今天我们吃蛋包饭"

    ql "好哎！我早就饿了，月咲小姐，我们先去吃饭吧"

    "月咲绫尝了一口蛋包饭，突然开始流泪"

    sd "哎？你怎么哭了？是我做的不和你口味吗？"

    ys "(摇头)不，我也不知道为什么"

    ys "这个味道我好像在哪里吃到过，但是，但是我想不起来了..."

    ql "没事的，不用担心，在你记忆恢复起来之前，就住在我们这里"

    ys "嗯！"

    "..."

    "......"

    "........."

    sd "啊，我吃饱了"

    ql "我也是"

    ys "我，我也吃饱了"

    ql "那行，就让哥哥收拾吧，月咲小姐今天就和哥哥一起睡吧"

    ql "走，我带你去哥哥房间"

    ys "嗯..."

    "说完,琴里便拉着月咲小姐上楼去了"

    "呼,赶快收拾一下去休息吧"

    "..."

    scene bg room

    "——士道房间"

    "我躺在床上,月咲小姐就睡在我的旁边,我丝毫没有意识到,我的人生即将迎来重大的改变"

    #第一章第二幕


    scene bg room

    "——早上，五河士道房间内"
    sd "(睁开眼睛)呼，感觉腰酸背痛的，不对，我怎么睡在地板上？？？"

    sd "(起身向床上看去)"

    "(月咲小姐在上面睡得正香)"

    sd "把她喊起来吧。"

    sd "(月咲小姐在上面睡得正香)算了，还是不叫醒你了，难得睡个好觉。"

    sd "(轻声)先去做早餐准备上学吧"

    sd "(不一会儿准备好了早餐)"

    sd "琴里，记得让月咲小姐呆在家里吃早餐，让她不要乱跑哦。"

    ql "(乖巧的点头)知道了，哥哥。"

    sd "我出门了。"

    ql "一路顺风"

    "简单打完招呼便向学校走去"

    "——来禅高中"

    scene bg school

    "——在教室内"

    "刚进教室殿町宏人便靠过来并在我耳边说"

    hm "士道，你听说了吗？"

    sd "听说什么？"

    hm "听说今天要来转校生，听说是一个美少女呢！"

    "殿町看起来兴致很高"

    sd "所以她是你的新目标吗？"

    sd "消息是真的吗？"

    hm "千真万确，不信的话待会开班会的时候就知道了。"

    "殿町看起来很自信"

    "闲聊了一会儿，小珠老师便走进教室了"

    xz "同学们准备一下，我们要开始今天的班会了。"

    "......"

    "班会上到一半..."

    xz "对了，今天有两位新同学转到我们班上"

    sd "(心中默念)两位？按道理来讲不应该是一位吗？"

    "正想着，小珠老师便向门外的两位转校生招了招手"

    xz "两位，进来吧"

    "两位转校生走了进来"

    sd "等等，这不是月咲小姐吗？"

    "月咲小姐穿着一身清新的校服，显得格外可爱，身旁还有一位是新面孔"

    "粉色的头发，穿着靴子，貌似还围了一条围巾在身上，看上去和披风一样，看起来很酷"

    sd "学校可以这么穿吗？"

    xz "好~，麻烦新同学做一下自我介绍"

    ys "大家好，我是月咲绫。"

    "众人" "这就没了？"

    sd "(真希望月咲小姐能早点恢复记忆啊)"

    "新面孔也跟着上前"

    sd "这位是？"

    hz "你们好呀，我叫立花火织，说完便微微微笑了起来"

    sd "(心中默念)看起来是位有趣的同学呢"

    xz "那个月咲同学和立花同学就坐在五河同学后面和旁边吧"

    "众人" "盯~~~"

    "于是乎，月咲坐在了我的右边，立花同学则是坐在了我的后面"

    sd "你好，月咲小姐"

    "月咲微微点头，算是回应"

    "立花同学则是很热情，主动与我打招呼"

    hz "你好呀，我是立花火织，很高兴认识你！"

    sd "谢。。谢谢"

    hz "(微微一笑)你的反应好有趣啊，士道君，你午休准备去哪里吃饭呢？(好奇)"

    menu:
        "去天台":
            $a = 1
            sd "我打算去天台，立花同学有什么打算吗?"

            hz "有趣的选择,我可以一起吗?"

            sd "火织还是和班上女生一起比较好吧"

            hz "哦?是吗?那我就听从你的建议了,嘻嘻"

            sd "(有种不好的预感)"

            "过了一段时间,我独自一人来到了天台上"

            "刚打开便当,有一道声音突然在我耳边响起"

            "???" "啊啦,啊啦,这不是五和同学吗?"

            sd "啊,你好,时崎同学"

            "这位是班上的时崎狂三同学,很少说话,坐在后排的她,带有一股特别的神秘感"

            "但是尽管如此,拥有较好面容的她依然是许多男生的追求对象"

            ks "五和同学也是上来享用午餐的吗,你的便当看起来很丰盛呢,是自己做的吗?"

            sd "是啊,毕竟父母总是在外面出差嘛,家里还有一个可爱的妹妹需要照顾"

            ks "五和同学还真是了不起呢，这厨艺可能1比班上大部分女同学还要好"

            ks "如果和你比的话，就连我也没什么自信了呢"

            sd "哪里哪里，言重了，时崎同学的手艺看上去也不差"

            hz "看来你们两位都是高手呢"

            "火织不知道从哪里冒出来加入了我们的对话"

            hz "可惜我的料理水平比较差呢，就只能吃面包了"

            "火织一边说着一边往我们这边投来羡慕的眼神"

            sd "立花同学要是不介意的话，要不要尝尝，我小心翼翼的询问"

            ks "既然如此，要不要也尝尝我的呢？立花同学"

            hz "你们两位真是好人呢，既然如此，我就恭敬不如从命了"

            "立花同学仔细的品尝了起来，一边点头一边露出幸福的笑容"

            hz "如果能取到你们二位其中一个，那他一定会很幸福吧"

            sd "太夸张了，立花同学也可以自己试着做一下，并没有很难"

            ks "是啊，就算你这样恭维我，也得不到什么好处哦"

            ks "总感觉天台上的时间流速和教室里不太一样呢"

            sd "是吗，我倒感觉没什么变化"

            ks "呆在这里,时间又快又慢，在教室里我只会觉得时间缓慢,果然时间是难以战胜的呢"

            hz "并不是这样的，时间是无法战胜的！没有人赢得了时间，连时间本身也不行"

            ks "并不是的，时间并不是无法战胜的。如果一个人一辈子初心都没有改变，那也算是战胜了时间经！历了时间的磨损内心依然如初，时间也会败下阵来"

            sd "是啊，时间真的好强大，但是我也觉得他并非无法战胜，并不是所有人都会被他的强大所改变"

            hz "看不出来，你们俩在这方面还挺心有灵犀，希望你们彼此都能够战胜时间"

            "我本来还想说些什么,但是刚好打了铃，午休要结束了。那时的我并不明白立花同学的话意味着什么"

            ks "那么二位，也许下个午休我们还能再见，祝你们好运！"

            "感觉她们两位对时间都挺敏感的"

        "留在教室":
            $a = 2
            sd "我打算留在教室，那里比较安静。"
            
        "去小卖部":
            $a = 3
            sd "我打算去小卖部，那里有好吃的。"
        
    "上课了"

    "我正在思考午休时的问题,坐在后面的立花同学突然戳了戳我的背"
    
    "我转过头去,但是还没来得及问就被老师点名站了起来"

    "老师" "请五河同学朗读一下这一页第二段的内容"

    "我一边读着一边听到立花同学微小的笑声"
    
    "看来被耍了,我无奈的叹了口气"

    "打铃了,周围的同学都开始陆续收拾东西准备放学回家"
    
    "我发现月咲同学只是呆呆坐在那儿无动于衷，简直就像一个机器人一样，没办法我走了过去"

    sd "那个......月咲小姐，不对，现在应该称呼为同学了，那么，月咲同学还不回家吗？"

    ys "回......家?我应该怎么做？"

    sd "唉，没办法，我来帮你吧"

    "我说着，一边帮她收拾东西，一边告诉她放学了学生应该怎么做"

    "在回家路上，月咲同学突然问了我几个很奇怪的问题"

    ys "我们现在是回家吗"

    sd "对啊"

    ys "我的家还是你的家呢"

    sd ".......暂且来讲应该是我们的家"

    ys "是吗，那是我们的家"

    "月咲同学说这句话的时候，轻轻笑了一下，但是那抹笑容很快就消失了"

    sd "是啊，是我们的家，不过有一天我会帮你找到真正的家的"

    ys "那可真是太感谢你了，士道"

    sd "晚上有什么想吃的吗？"

    ys "蛋包饭！（几乎是秒答）"

    sd "好，你喜欢的话就天天做，话说回来今天在学校感觉怎么样？有没有同学或者老师为难你"

    ys "大部分女生想和我交朋友，男生有一部分人让我离你远一点"

    sd "哈哈......这样吗，遇到困难记得和我说，我会尽我所能帮助你的"

    scene bg room

    sd "我回来了"

    "我把门推开，琴里和我们热情的打招呼"

    ql "哥哥和绫姐姐，欢迎回来，今天晚上吃什么？"

    sd "月咲小姐想吃蛋包饭，没问题吧？"

    ql "好哦，月咲姐姐想吃的话没问题"

    sd "好，你们稍等，我去准备"

    "不知道月咲小姐在我们这里待多久呢，失去了记忆一定很痛苦吧，不知道她的家人着不着急"

    "我一边准备晚饭，一边思考"

    "算了，还是赶快准备吧，她们可能饿了"

    scene bg room

    "饭桌上，琴里不停地找月咲小姐谈话，已经好到了称呼名字"

    ql "绫姐姐，你特别喜欢吃蛋包饭吗"

    ys "嗯"

    ql "每天都想吃吗"

    ys "嗯"

    sd "......看来还要相处很久呢，不过琴里也很开心，也没什么问题，多个姐姐好像也不错"

    ""


    return
