# Author-Topic Modeling with news
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

Generating author-topic model...
Completed in 459.6195 seconds

Topics
Topic 0: 0.001*"like" + 0.001*"year" + 0.001*"compani" + 0.001*"new" + 0.001*"peopl" + 0.001*"experi" + 0.001*"time" + 0.001*"way" + 0.001*"work" + 0.001*"go"
Topic 1: 0.011*"like" + 0.010*"peopl" + 0.008*"percent" + 0.008*"clinton" + 0.008*"polit" + 0.008*"american" + 0.007*"think" + 0.007*"state" + 0.006*"way" + 0.006*"time"
Topic 2: 0.001*"futur" + 0.001*"peopl" + 0.001*"compani" + 0.001*"like" + 0.001*"year" + 0.001*"new" + 0.001*"group" + 0.001*"world" + 0.001*"work" + 0.001*"way"
Topic 3: 0.001*"stori" + 0.001*"audienc" + 0.001*"like" + 0.001*"season" + 0.001*"way" + 0.001*"new" + 0.001*"go" + 0.001*"play" + 0.001*"peopl" + 0.001*"want"
Topic 4: 0.001*"new" + 0.001*"california" + 0.001*"presid" + 0.001*"time" + 0.001*"peopl" + 0.001*"year" + 0.001*"break" + 0.001*"southern" + 0.001*"credit" + 0.001*"los"
Topic 5: 0.001*"new" + 0.001*"peopl" + 0.001*"break" + 0.001*"california" + 0.001*"learn" + 0.001*"program" + 0.001*"presid" + 0.001*"polic" + 0.001*"compani" + 0.001*"health"
Topic 6: 0.001*"com" + 0.001*"point" + 0.001*"time" + 0.001*"report" + 0.001*"peopl" + 0.001*"like" + 0.001*"presid" + 0.001*"go" + 0.001*"new" + 0.001*"come"
Topic 7: 0.018*"compani" + 0.017*"percent" + 0.016*"busi" + 0.015*"market" + 0.014*"year" + 0.013*"news" + 0.012*"new" + 0.012*"world" + 0.010*"product" + 0.009*"invest"
Topic 8: 0.050*"trump" + 0.021*"presid" + 0.017*"state" + 0.016*"news" + 0.014*"republican" + 0.010*"elect" + 0.009*"democrat" + 0.008*"senat" + 0.008*"report" + 0.008*"unit"
Topic 9: 0.001*"publish" + 0.001*"compani" + 0.001*"articl" + 0.001*"like" + 0.001*"year" + 0.001*"facebook" + 0.001*"time" + 0.001*"futur" + 0.001*"member" + 0.001*"group"
Topic 10: 0.001*"california" + 0.001*"year" + 0.001*"break" + 0.001*"presid" + 0.001*"time" + 0.001*"go" + 0.001*"new" + 0.001*"peopl" + 0.001*"member" + 0.001*"credit"
Topic 11: 0.013*"like" + 0.010*"peopl" + 0.009*"time" + 0.009*"new" + 0.008*"work" + 0.008*"mr" + 0.008*"year" + 0.006*"know" + 0.006*"way" + 0.005*"come"
Topic 12: 0.001*"time" + 0.001*"california" + 0.001*"year" + 0.001*"game" + 0.001*"night" + 0.001*"new" + 0.001*"like" + 0.001*"come" + 0.001*"presid" + 0.001*"write"
Topic 13: 0.039*"mr" + 0.013*"year" + 0.009*"ms" + 0.009*"state" + 0.008*"time" + 0.008*"new" + 0.006*"trump" + 0.005*"go" + 0.005*"presid" + 0.005*"like"
Topic 14: 0.001*"stori" + 0.001*"like" + 0.001*"new" + 0.001*"play" + 0.001*"time" + 0.001*"audienc" + 0.001*"year" + 0.001*"way" + 0.001*"learn" + 0.001*"chang"
Topic 15: 0.001*"think" + 0.001*"like" + 0.001*"facebook" + 0.001*"peopl" + 0.001*"work" + 0.001*"compani" + 0.001*"video" + 0.001*"year" + 0.001*"time" + 0.001*"new"
Topic 16: 0.001*"like" + 0.001*"year" + 0.001*"peopl" + 0.001*"futur" + 0.001*"think" + 0.001*"new" + 0.001*"technolog" + 0.001*"time" + 0.001*"go" + 0.001*"compani"
Topic 17: 0.001*"way" + 0.001*"stori" + 0.001*"new" + 0.001*"chang" + 0.001*"like" + 0.001*"seri" + 0.001*"go" + 0.001*"audienc" + 0.001*"time" + 0.001*"year"
Topic 18: 0.001*"peopl" + 0.001*"year" + 0.001*"like" + 0.001*"think" + 0.001*"new" + 0.001*"game" + 0.001*"know" + 0.001*"california" + 0.001*"go" + 0.001*"way"
Topic 19: 0.001*"break" + 0.001*"california" + 0.001*"new" + 0.001*"presid" + 0.001*"stori" + 0.001*"go" + 0.001*"season" + 0.001*"credit" + 0.001*"like" + 0.001*"year"

Authors
Atlantic: [(1, 0.10875012464858978), (7, 0.14067014676601375), (8, 0.18599926482896606), (11, 0.4175300344520529), (13, 0.14705019035160263)]
Breitbart: [(1, 0.2731924005934917), (8, 0.37689343318576757), (13, 0.34991400150939567)]
Business Insider: [(1, 0.08087457352705688), (7, 0.3742080679438949), (8, 0.15678970808887677), (11, 0.21329078061903026), (13, 0.1748359112530885)]
Buzzfeed News: [(1, 0.020719256067199505), (7, 0.11587774074620137), (8, 0.1514694445290248), (11, 0.4328217845791814), (13, 0.2791115048717695)]
CNN: [(11, 0.3551065097187259), (13, 0.6448918462191309)]
Fox News: [(1, 0.1723217461879092), (8, 0.3799011516308513), (11, 0.196911122386663), (13, 0.2508651493198188)]
Guardian: [(1, 0.07741067211197308), (7, 0.12765308556807373), (8, 0.06975574775359158), (11, 0.2886286191094665), (13, 0.43655141068366154)]
Los Angeles Times: [(13, 0.999999747255228)]
NPR: [(1, 0.07519967015345466), (7, 0.1052365443338872), (8, 0.15124424712781517), (11, 0.49427257447405865), (13, 0.17404671298797192)]
National Review: [(1, 0.4072499730680655), (7, 0.08082303891262806), (8, 0.2895497590187106), (11, 0.21995323547383328)]
New Inquiry: [(1, 0.21369632062140212), (7, 0.013453954515743341), (11, 0.7725574685206353)]
New York Post: [(7, 0.25568774572195957), (8, 0.05033874264189447), (11, 0.047426601049772386), (13, 0.6405207999776257)]
New York Times: [(7, 0.048894443379238164), (8, 0.04909970914188271), (11, 0.3829076592338849), (13, 0.5190981091411889)]
Reuters: [(7, 0.5268020705903462), (8, 0.47319760351667955)]
Talking Points Memo: [(1, 0.2806209615490172), (7, 0.063504823058292), (8, 0.6307619131517669), (11, 0.02511063459684568)]
Verge: [(1, 0.9999980416448859)]
Vox: [(1, 0.4367263248855388), (8, 0.09179398447214145), (11, 0.4676710351221586)]
Washington Post: [(1, 0.11597187344877195), (8, 0.28426712148481753), (11, 0.3601061920905911), (13, 0.2396545433515537)]
```
