# Topic Modeling with news
To run this experiment, your need to download the dataset [here](https://components.one/datasets/all-the-news-articles-dataset/), because its size exceed 100 MB and can not be uploaded in GitHub.

Output:
```python
Loading data...
Completed in 26.1246 seconds

Pre-processing...
Completed in 1243.7947 seconds

Extracting dictionary...
Completed in 69.2948 seconds

Extracting features...
Completed in 43.9467 seconds

Generating topic model...
Completed in 190.7270 seconds

Topic 0: 0.022*"north" + 0.020*"china" + 0.012*"reuter" + 0.010*"south" + 0.009*"news" + 0.008*"test" + 0.007*"militari" + 0.005*"launch" + 0.005*"unit" + 0.005*"weapon"

Topic 1: 0.017*"water" + 0.009*"citi" + 0.008*"resid" + 0.008*"area" + 0.006*"build" + 0.006*"home" + 0.006*"mile" + 0.006*"mr" + 0.006*"town" + 0.005*"park"

Topic 2: 0.012*"islam" + 0.008*"militari" + 0.008*"muslim" + 0.008*"war" + 0.007*"attack" + 0.006*"state" + 0.006*"trump" + 0.006*"forc" + 0.006*"govern" + 0.006*"unit"

Topic 3: 0.007*"book" + 0.006*"love" + 0.005*"women" + 0.005*"life" + 0.005*"music" + 0.005*"like" + 0.005*"stori" + 0.004*"feel" + 0.004*"write" + 0.004*"charact"

Topic 4: 0.020*"gun" + 0.019*"tax" + 0.016*"protest" + 0.012*"mr" + 0.007*"republican" + 0.007*"trump" + 0.007*"senat" + 0.006*"polic" + 0.005*"violenc" + 0.005*"legisl"

Topic 5: 0.010*"court" + 0.008*"law" + 0.007*"feder" + 0.007*"student" + 0.006*"immigr" + 0.006*"school" + 0.006*"justic" + 0.006*"judg" + 0.006*"mr" + 0.005*"case"

Topic 6: 0.061*"mr" + 0.030*"ms" + 0.010*"art" + 0.005*"york" + 0.004*"citi" + 0.004*"work" + 0.004*"new" + 0.004*"design" + 0.004*"music" + 0.003*"hous"

Topic 7: 0.013*"compani" + 0.011*"reuter" + 0.010*"percent" + 0.010*"news" + 0.009*"market" + 0.008*"billion" + 0.007*"busi" + 0.007*"bank" + 0.007*"price" + 0.006*"stock"

Topic 8: 0.015*"car" + 0.009*"space" + 0.009*"mr" + 0.009*"room" + 0.007*"park" + 0.007*"build" + 0.007*"design" + 0.007*"citi" + 0.006*"drive" + 0.006*"price"

Topic 9: 0.022*"film" + 0.016*"mr" + 0.015*"movi" + 0.011*"music" + 0.008*"star" + 0.007*"charact" + 0.007*"play" + 0.007*"ms" + 0.006*"perform" + 0.006*"seri"

Topic 10: 0.029*"california" + 0.023*"los" + 0.021*"angel" + 0.015*"san" + 0.011*"editor" + 0.011*"york" + 0.008*"today" + 0.008*"mr" + 0.008*"time" + 0.006*"new"

Topic 11: 0.022*"polic" + 0.009*"shoot" + 0.009*"offic" + 0.008*"kill" + 0.008*"attack" + 0.007*"arrest" + 0.007*"investig" + 0.006*"victim" + 0.006*"charg" + 0.005*"man"

Topic 12: 0.018*"facebook" + 0.013*"mr" + 0.010*"fox" + 0.008*"twitter" + 0.008*"compani" + 0.007*"sexual" + 0.007*"news" + 0.006*"post" + 0.006*"network" + 0.006*"tweet"

Topic 13: 0.026*"game" + 0.019*"player" + 0.018*"season" + 0.016*"team" + 0.011*"play" + 0.009*"win" + 0.007*"fan" + 0.006*"final" + 0.006*"second" + 0.005*"round"

Topic 14: 0.024*"trump" + 0.014*"clinton" + 0.011*"republican" + 0.008*"democrat" + 0.007*"campaign" + 0.007*"presid" + 0.007*"elect" + 0.007*"vote" + 0.007*"senat" + 0.006*"voter"

Topic 15: 0.010*"studi" + 0.009*"research" + 0.006*"health" + 0.006*"food" + 0.005*"medic" + 0.005*"drug" + 0.005*"univers" + 0.005*"scienc" + 0.004*"human" + 0.004*"women"

Topic 16: 0.021*"mr" + 0.019*"european" + 0.012*"union" + 0.012*"minist" + 0.011*"parti" + 0.010*"vote" + 0.010*"europ" + 0.009*"prime" + 0.007*"trade" + 0.006*"leader"

Topic 17: 0.011*"ms" + 0.010*"famili" + 0.010*"mother" + 0.009*"children" + 0.009*"father" + 0.008*"daughter" + 0.007*"mr" + 0.007*"son" + 0.007*"girl" + 0.007*"school"

Topic 18: 0.033*"russian" + 0.031*"russia" + 0.019*"mr" + 0.012*"intellig" + 0.010*"trump" + 0.008*"offici" + 0.008*"investig" + 0.006*"presid" + 0.006*"agenc" + 0.005*"secur"

Topic 19: 0.016*"practic" + 0.010*"hospit" + 0.010*"game" + 0.007*"california" + 0.007*"season" + 0.007*"updat" + 0.006*"angel" + 0.005*"play" + 0.005*"los" + 0.005*"team"
```