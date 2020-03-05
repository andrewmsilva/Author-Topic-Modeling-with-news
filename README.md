# Topic Modeling with news
To run this experiment, your need to download the dataset [here](https://components.one/datasets/all-the-news-articles-dataset/), because its size exceed 100 MB and can not be uploaded in GitHub.

Output:
```python
Data loading: 31.7564 seconds
Pre-processing: 1087.4770 seconds
Feature extraction: 124.5102 seconds
LDA generating: 467.6802 seconds

Topic 0: 0.025*"soccer" + 0.015*"manchest" + 0.014*"stein" + 0.013*"player" + 0.013*"fifa" + 0.013*"leagu" + 0.012*"team" + 0.010*"barcelona" + 0.010*"abedi" + 0.010*"club"

Topic 1: 0.021*"airlin" + 0.017*"flight" + 0.012*"passeng" + 0.010*"airport" + 0.009*"mnuchin" + 0.009*"plane" + 0.009*"bitcoin" + 0.008*"fargo" + 0.007*"well" + 0.007*"hacker"

Topic 2: 0.010*"bedroom" + 0.010*"food" + 0.009*"cook" + 0.008*"restaur" + 0.007*"kitchen" + 0.006*"chef" + 0.006*"recip" + 0.006*"bath" + 0.006*"wine" + 0.006*"room"

Topic 3: 0.019*"mateen" + 0.019*"labour" + 0.018*"airbnb" + 0.014*"orlando" + 0.011*"shark" + 0.009*"zimbabw" + 0.009*"noor" + 0.009*"princ" + 0.008*"allig" + 0.007*"princess"

Topic 4: 0.049*"pruitt" + 0.030*"thiel" + 0.017*"gottlieb" + 0.015*"durst" + 0.014*"zimmerman" + 0.011*"palantir" + 0.011*"macdonald" + 0.011*"berman" + 0.010*"pérez" + 0.009*"fyre"

Topic 5: 0.039*"tesla" + 0.032*"vehicl" + 0.025*"automak" + 0.024*"car" + 0.023*"blasio" + 0.018*"electr" + 0.015*"model" + 0.015*"musk" + 0.014*"kong" + 0.013*"motor"

Topic 6: 0.008*"music" + 0.005*"song" + 0.004*"artist" + 0.004*"perform" + 0.004*"album" + 0.004*"play" + 0.003*"theater" + 0.003*"film" + 0.003*"danc" + 0.003*"love"

Topic 7: 0.027*"israel" + 0.027*"saudi" + 0.026*"iran" + 0.021*"isra" + 0.020*"palestinian" + 0.014*"arabia" + 0.012*"netanyahu" + 0.011*"jerusalem" + 0.011*"iranian" + 0.010*"jewish"

Topic 8: 0.003*"women" + 0.003*"book" + 0.003*"school" + 0.002*"student" + 0.002*"work" + 0.002*"write" + 0.002*"life" + 0.002*"stori" + 0.002*"black" + 0.002*"feel"

Topic 9: 0.008*"compani" + 0.007*"percent" + 0.005*"market" + 0.005*"news" + 0.005*"billion" + 0.004*"busi" + 0.004*"price" + 0.004*"bank" + 0.004*"invest" + 0.004*"stock"

Topic 10: 0.034*"yahoo" + 0.025*"egypt" + 0.024*"mulvaney" + 0.024*"qatar" + 0.021*"egyptian" + 0.018*"redston" + 0.016*"sisi" + 0.014*"viacom" + 0.013*"podesta" + 0.013*"cairo"

Topic 11: 0.009*"trump" + 0.005*"deleg" + 0.004*"cruz" + 0.004*"gorsuch" + 0.003*"court" + 0.003*"reuter" + 0.003*"suprem" + 0.003*"muslim" + 0.003*"senat" + 0.003*"conserv"

Topic 12: 0.086*"olymp" + 0.047*"athlet" + 0.031*"medal" + 0.023*"dope" + 0.021*"sport" + 0.018*"goldman" + 0.017*"gold" + 0.016*"game" + 0.015*"chaffetz" + 0.012*"swim"

Topic 13: 0.025*"navi" + 0.024*"ship" + 0.017*"volkswagen" + 0.016*"drone" + 0.014*"amtrak" + 0.013*"diesel" + 0.011*"fisher" + 0.011*"vessel" + 0.009*"creditor" + 0.009*"naval"

Topic 14: 0.028*"korea" + 0.022*"north" + 0.016*"korean" + 0.012*"missil" + 0.012*"nuclear" + 0.009*"south" + 0.009*"storm" + 0.009*"hurrican" + 0.005*"flood" + 0.005*"pyongyang"

Topic 15: 0.011*"russia" + 0.011*"trump" + 0.011*"russian" + 0.009*"comey" + 0.007*"investig" + 0.006*"intellig" + 0.005*"putin" + 0.005*"presid" + 0.004*"committe" + 0.004*"flynn"

Topic 16: 0.017*"nasa" + 0.014*"space" + 0.012*"earth" + 0.012*"planet" + 0.011*"moon" + 0.010*"eclips" + 0.009*"orbit" + 0.008*"solar" + 0.008*"astronom" + 0.008*"rocket"

Topic 17: 0.113*"abort" + 0.031*"parenthood" + 0.026*"contracept" + 0.023*"pregnanc" + 0.020*"women" + 0.018*"clinic" + 0.013*"reproduct" + 0.010*"manson" + 0.009*"wade" + 0.009*"bondi"

Topic 18: 0.082*"appl" + 0.043*"iphon" + 0.031*"samsung" + 0.023*"cuomo" + 0.023*"googl" + 0.022*"phone" + 0.019*"smartphon" + 0.018*"devic" + 0.016*"waymo" + 0.012*"alphabet"

Topic 19: 0.025*"mexico" + 0.019*"cuba" + 0.017*"mexican" + 0.016*"cuban" + 0.013*"castro" + 0.013*"border" + 0.008*"nieto" + 0.008*"shkreli" + 0.007*"havana" + 0.006*"undocu"

Topic 20: 0.007*"polic" + 0.004*"shoot" + 0.003*"citi" + 0.003*"offic" + 0.003*"kill" + 0.003*"attack" + 0.002*"famili" + 0.002*"home" + 0.002*"street" + 0.002*"arrest"

Topic 21: 0.025*"guantanamo" + 0.023*"thai" + 0.022*"sailor" + 0.018*"robart" + 0.018*"be" + 0.013*"sandov" + 0.012*"submarin" + 0.011*"peltz" + 0.010*"chattanooga" + 0.009*"rapp"

Topic 22: 0.038*"yanke" + 0.025*"met" + 0.024*"basebal" + 0.021*"inning" + 0.019*"game" + 0.016*"pitch" + 0.015*"leagu" + 0.014*"dodger" + 0.014*"pitcher" + 0.013*"season"

Topic 23: 0.053*"friedman" + 0.039*"rosenstein" + 0.036*"ossoff" + 0.019*"karen" + 0.018*"grassley" + 0.015*"porzingi" + 0.015*"mcgahn" + 0.013*"brownback" + 0.012*"lynch" + 0.010*"mcadoo"

Topic 24: 0.045*"rouhani" + 0.026*"palin" + 0.019*"tehran" + 0.017*"ranger" + 0.016*"mali" + 0.015*"khamenei" + 0.015*"niger" + 0.011*"cpac" + 0.010*"lundqvist" + 0.010*"valentin"

Topic 25: 0.016*"game" + 0.014*"player" + 0.012*"team" + 0.010*"coach" + 0.010*"season" + 0.009*"leagu" + 0.007*"footbal" + 0.007*"play" + 0.006*"sport" + 0.005*"playoff"

Topic 26: 0.020*"syria" + 0.018*"syrian" + 0.016*"islam" + 0.012*"militari" + 0.011*"assad" + 0.011*"rebel" + 0.010*"iraqi" + 0.010*"forc" + 0.010*"milit" + 0.010*"iraq"

Topic 27: 0.040*"drug" + 0.037*"patient" + 0.024*"opioid" + 0.024*"marijuana" + 0.023*"medic" + 0.019*"doctor" + 0.017*"cancer" + 0.016*"treatment" + 0.014*"hospit" + 0.013*"addict"

Topic 28: 0.009*"comedi" + 0.006*"colbert" + 0.006*"episod" + 0.005*"cake" + 0.005*"baldwin" + 0.005*"joke" + 0.004*"comedian" + 0.004*"night" + 0.004*"kimmel" + 0.004*"season"

Topic 29: 0.083*"afghan" + 0.061*"taliban" + 0.053*"afghanistan" + 0.039*"kabul" + 0.023*"ghani" + 0.018*"scalis" + 0.013*"indonesia" + 0.012*"pakistan" + 0.012*"nike" + 0.012*"jakarta"

Topic 30: 0.027*"reilli" + 0.023*"tenni" + 0.022*"ail" + 0.018*"murdoch" + 0.016*"wimbledon" + 0.016*"gymnast" + 0.015*"pasqual" + 0.012*"tournament" + 0.012*"match" + 0.012*"nadal"

Topic 31: 0.043*"kain" + 0.016*"tournament" + 0.015*"duke" + 0.014*"seed" + 0.013*"coulter" + 0.011*"baylor" + 0.011*"ncaa" + 0.010*"gonzaga" + 0.009*"villanova" + 0.009*"trooper"

Topic 32: 0.083*"manafort" + 0.030*"biden" + 0.021*"shabab" + 0.014*"mann" + 0.013*"toomey" + 0.013*"wework" + 0.012*"lepag" + 0.011*"loeb" + 0.010*"farook" + 0.010*"sabathia"

Topic 33: 0.026*"film" + 0.021*"movi" + 0.008*"oscar" + 0.007*"charact" + 0.006*"actor" + 0.006*"hollywood" + 0.006*"award" + 0.006*"star" + 0.005*"comic" + 0.005*"theater"

Topic 34: 0.036*"climat" + 0.017*"emiss" + 0.016*"coal" + 0.015*"water" + 0.015*"environment" + 0.014*"energi" + 0.013*"carbon" + 0.011*"pollut" + 0.009*"plant" + 0.009*"warm"

Topic 35: 0.073*"weinstein" + 0.034*"somali" + 0.031*"berkshir" + 0.022*"gillespi" + 0.015*"corcoran" + 0.014*"blackston" + 0.013*"kabila" + 0.012*"schwarzman" + 0.012*"dimon" + 0.011*"barron"

Topic 36: 0.073*"rohingya" + 0.061*"myanmar" + 0.021*"rakhin" + 0.015*"wray" + 0.014*"bangladesh" + 0.013*"abdeslam" + 0.013*"emoji" + 0.012*"wolff" + 0.012*"buddhist" + 0.012*"farag"

Topic 37: 0.017*"trump" + 0.009*"clinton" + 0.007*"republican" + 0.006*"democrat" + 0.005*"voter" + 0.005*"vote" + 0.005*"elect" + 0.005*"campaign" + 0.005*"presid" + 0.005*"parti"

Topic 38: 0.043*"cosbi" + 0.022*"catalan" + 0.018*"catalonia" + 0.016*"constand" + 0.009*"mercer" + 0.009*"neill" + 0.009*"bowi" + 0.008*"lamar" + 0.008*"assault" + 0.008*"dementia"

Topic 39: 0.029*"pipelin" + 0.021*"tribe" + 0.019*"nassar" + 0.016*"dakota" + 0.010*"marawi" + 0.010*"newman" + 0.010*"sioux" + 0.010*"indigen" + 0.009*"indian" + 0.009*"nativ"

Topic 40: 0.007*"court" + 0.004*"immigr" + 0.004*"judg" + 0.004*"case" + 0.004*"justic" + 0.004*"state" + 0.003*"feder" + 0.003*"lawyer" + 0.003*"legal" + 0.003*"rule"

Topic 41: 0.022*"ballet" + 0.019*"fillon" + 0.016*"kenya" + 0.015*"ampt" + 0.014*"castil" + 0.014*"autism" + 0.012*"kenyatta" + 0.012*"coutur" + 0.012*"cabl" + 0.011*"kenyan"

Topic 42: 0.057*"uber" + 0.022*"maduro" + 0.021*"venezuela" + 0.019*"driver" + 0.014*"kalanick" + 0.013*"autonom" + 0.013*"robot" + 0.013*"venezuelan" + 0.013*"car" + 0.012*"vehicl"

Topic 43: 0.026*"mccrori" + 0.022*"bezo" + 0.019*"weiner" + 0.017*"mcmaster" + 0.016*"churchil" + 0.014*"mcfarland" + 0.011*"hungarian" + 0.011*"hungari" + 0.011*"parasit" + 0.011*"larsen"

Topic 44: 0.106*"mosul" + 0.060*"isi" + 0.030*"kurdish" + 0.018*"airstrik" + 0.018*"convoy" + 0.016*"mice" + 0.016*"schwartz" + 0.014*"iraqi" + 0.014*"isil" + 0.013*"katz"

Topic 45: 0.018*"sauc" + 0.016*"taiwan" + 0.014*"chees" + 0.014*"menu" + 0.013*"china" + 0.012*"salad" + 0.012*"fri" + 0.011*"pork" + 0.010*"beef" + 0.010*"tomato"

Topic 46: 0.017*"insur" + 0.016*"health" + 0.014*"republican" + 0.013*"senat" + 0.011*"care" + 0.009*"medicaid" + 0.009*"repeal" + 0.009*"obamacar" + 0.008*"budget" + 0.007*"legisl"

Topic 47: 0.014*"reuter" + 0.009*"china" + 0.007*"european" + 0.006*"britain" + 0.005*"minist" + 0.004*"chines" + 0.004*"europ" + 0.004*"trade" + 0.004*"macron" + 0.004*"germani"

Topic 48: 0.008*"studi" + 0.008*"research" + 0.007*"diseas" + 0.006*"zika" + 0.006*"health" + 0.006*"brain" + 0.005*"anim" + 0.005*"virus" + 0.004*"scientist" + 0.004*"infect"

Topic 49: 0.025*"gerrymand" + 0.021*"menendez" + 0.015*"aborigin" + 0.015*"caesar" + 0.013*"jeter" + 0.012*"einstein" + 0.011*"fossil" + 0.011*"redistrict" + 0.011*"neanderth" + 0.010*"gillibrand"
```