# Author-Topic Modeling with news
To run this experiment, your need to download the dataset [here](https://components.one/datasets/all-the-news-articles-dataset/), because its size exceed 100 MB and can not be uploaded in GitHub.

Output:
```python
Loading data...
Completed in 26.1246 seconds

Pre-processing...
Completed in 509.2679 seconds

Extracting dictionary...
Completed in 65.9431 seconds

Extracting features...
Completed in 49.9549 seconds

Generating author-topic model...
Completed in 456.2367 seconds

Topics
Topic 0: 0.000*"think" + 0.000*"people" + 0.000*"company" + 0.000*"time" + 0.000*"build" + 0.000*"like" + 0.000*"new" + 0.000*"imagine" + 0.000*"go" + 0.000*"facebook"
Topic 1: 0.032*"news" + 0.016*"reuters" + 0.010*"trump" + 0.008*"business" + 0.008*"world" + 0.007*"percent" + 0.007*"state" + 0.007*"market" + 0.006*"president" + 0.006*"company"
Topic 2: 0.010*"president" + 0.008*"trump" + 0.007*"year" + 0.007*"new" + 0.006*"house" + 0.006*"state" + 0.005*"time" + 0.005*"city" + 0.005*"officials" + 0.005*"include"
Topic 3: 0.000*"like" + 0.000*"company" + 0.000*"facebook" + 0.000*"super" + 0.000*"article" + 0.000*"people" + 0.000*"work" + 0.000*"time" + 0.000*"new" + 0.000*"hammer"
Topic 4: 0.037*"trump" + 0.012*"state" + 0.011*"president" + 0.007*"clinton" + 0.006*"campaign" + 0.006*"vote" + 0.006*"republican" + 0.005*"party" + 0.005*"house" + 0.005*"republicans"
Topic 5: 0.000*"like" + 0.000*"company" + 0.000*"future" + 0.000*"group" + 0.000*"facebook" + 0.000*"article" + 0.000*"new" + 0.000*"work" + 0.000*"year" + 0.000*"people"
Topic 6: 0.000*"like" + 0.000*"time" + 0.000*"company" + 0.000*"people" + 0.000*"work" + 0.000*"new" + 0.000*"think" + 0.000*"game" + 0.000*"go" + 0.000*"want"
Topic 7: 0.000*"like" + 0.000*"people" + 0.000*"company" + 0.000*"new" + 0.000*"work" + 0.000*"time" + 0.000*"think" + 0.000*"year" + 0.000*"world" + 0.000*"go"
Topic 8: 0.000*"like" + 0.000*"new" + 0.000*"time" + 0.000*"rat" + 0.000*"people" + 0.000*"go" + 0.000*"think" + 0.000*"company" + 0.000*"tell" + 0.000*"get"
Topic 9: 0.000*"super" + 0.000*"like" + 0.000*"peak" + 0.000*"new" + 0.000*"time" + 0.000*"play" + 0.000*"facebook" + 0.000*"learn" + 0.000*"company" + 0.000*"story"
Topic 10: 0.000*"star" + 0.000*"time" + 0.000*"new" + 0.000*"like" + 0.000*"play" + 0.000*"war" + 0.000*"fan" + 0.000*"years" + 0.000*"film" + 0.000*"year"
Topic 11: 0.000*"like" + 0.000*"company" + 0.000*"new" + 0.000*"work" + 0.000*"go" + 0.000*"build" + 0.000*"time" + 0.000*"people" + 0.000*"think" + 0.000*"come"
Topic 12: 0.000*"archiveteam" + 0.000*"like" + 0.000*"company" + 0.000*"people" + 0.000*"new" + 0.000*"time" + 0.000*"write" + 0.000*"work" + 0.000*"year" + 0.000*"article"
Topic 13: 0.000*"roof" + 0.000*"republicans" + 0.000*"trump" + 0.000*"president" + 0.000*"jury" + 0.000*"penalty" + 0.000*"house" + 0.000*"elect" + 0.000*"new" + 0.000*"death"
Topic 14: 0.000*"like" + 0.000*"play" + 0.000*"company" + 0.000*"game" + 0.000*"time" + 0.000*"year" + 0.000*"go" + 0.000*"people" + 0.000*"point" + 0.000*"new"
Topic 15: 0.000*"archiveteam" + 0.000*"company" + 0.000*"article" + 0.000*"facebook" + 0.000*"time" + 0.000*"future" + 0.000*"like" + 0.000*"new" + 0.000*"group" + 0.000*"story"
Topic 16: 0.000*"new" + 0.000*"star" + 0.000*"time" + 0.000*"war" + 0.000*"film" + 0.000*"like" + 0.000*"president" + 0.000*"year" + 0.000*"california" + 0.000*"go"
Topic 17: 0.000*"like" + 0.000*"company" + 0.000*"new" + 0.000*"time" + 0.000*"play" + 0.000*"future" + 0.000*"work" + 0.000*"peak" + 0.000*"series" + 0.000*"world"
Topic 18: 0.008*"like" + 0.007*"people" + 0.007*"time" + 0.006*"new" + 0.006*"work" + 0.004*"know" + 0.004*"think" + 0.004*"years" + 0.004*"come" + 0.004*"company"
Topic 19: 0.000*"super" + 0.000*"company" + 0.000*"like" + 0.000*"peak" + 0.000*"series" + 0.000*"twin" + 0.000*"audience" + 0.000*"story" + 0.000*"new" + 0.000*"way"

Authors
Atlantic: [(1, 0.13489067990565592), (4, 0.18839292630930504), (18, 0.6767161959710996)]
Breitbart: [(1, 0.29799298152831155), (4, 0.4335391737782584), (18, 0.26846771968077104)]
Business Insider: [(1, 0.192148003506914), (2, 0.16268195049523404), (4, 0.059202141979552605), (18, 0.5859671234249043)]
Buzzfeed News: [(1, 0.2215782755835477), (2, 0.17580666880682733), (4, 0.027404137520933645), (18, 0.5752107089739609)]
CNN: [(2, 0.15005749035362717), (4, 0.12172922725972929), (18, 0.7282121107017211)]
Fox News: [(1, 0.2102483579043843), (2, 0.16979705286534405), (4, 0.24275107016720313), (18, 0.3772028841210182)]
Guardian: [(1, 0.03524077243239725), (2, 0.18214691571844802), (4, 0.08686080833616482), (18, 0.6957511418569182)]
Los Angeles Times: [(2, 0.3569280229386201), (18, 0.643071796719256)]
NPR: [(1, 0.14530407813818455), (2, 0.10556457425998919), (4, 0.08709155537075787), (18, 0.6620395926837375)]
National Review: [(1, 0.2304787732462771), (4, 0.2984528914627512), (18, 0.471067933907511)]
New Inquiry: [(4, 0.012220603953133374), (18, 0.9798873273442711)]
New York Post: [(2, 0.29322574802992185), (4, 0.07012980549070219), (18, 0.6366440944413583)]
New York Times: [(2, 0.3263687567981592), (4, 0.0664838802498542), (18, 0.6071473001122365)]
Reuters: [(1, 0.700534208707511), (2, 0.230403748281423), (18, 0.06865764232895494)]
Talking Points Memo: [(1, 0.18095813029479538), (4, 0.6553995328587564), (18, 0.15581157234643817)]
Verge: [(1, 0.9999985143505521)]
Vox: [(4, 0.24962176583802886), (18, 0.7503779726580149)]
Washington Post: [(2, 0.21448407259738134), (4, 0.32656169053710976), (18, 0.4589540187419434)]
```
