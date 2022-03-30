# Bengali AI Handwritten Grapheme Classification
> 이유한님의 유튜브를 보면서 공부한 내용들을 정리

## Overview
### Description
벵골어는 수억명의 사용자를 가진 세계에서 다섯 번째로 많이 사용되는 언어이다. 방글라데시의 공용어이고, 인도에서 두 번째로 많이 사용되는 언어이다. 이것을 고려해봤을 때, 손으로 쓴 언어의 이미지를 광학적으로 인식할 수 있는 AI를 개발하는 데에 사업적, 교육적으로 상당한 관심이 있다.

광학 문자 인식은 벵골어에게 있어 특히 어렵다. 벵골어는 49개의 글자(모음: 11개, 자음: 38개)를 가지고 있지만, 18개의 잠재적인 억양이 있다. 이것은 가장 작은 단위인 문자소(grapheme)가 많다는 것을 의미한다. 더해진 복잡성은 최대 13000개의 문자소 변형이 발생한다.(영어의 경우 250개의 graphemic units)

이 대회에서는 손으로 쓴 벵골어 문자 이미지가 제공된다. 이미지에서 세 가지 구성 요소(grapheme root, vowel diacritics and consonant diacritics)를 개별적으로 분류해야 한다.

### Evaluation
결과는 hierarchical macro-averaged recall을 사용하여 평가한다. 첫번째로, 각 성분(grapheme root, vowel diacritics and consonant diacritics)에 대해 표준 macro-averaged recall이 계산된다. 최종 점수는 각 성분에 대한 3개 점수의 가중치 평균으로, grapheme root에는 이중 가중치가 부여된다. 
```
import numpy as np
import sklearn.metrics

scores = []
for component in ['grapheme_root', 'consonant_diacritic', 'vowel_diacritic']:
    y_true_subset = solution[solution[component] == component]['target'].values
    y_pred_subset = submission[submission[component] == component]['target'].values
    scores.append(sklearn.metrics.recall_score(
        y_true_subset, y_pred_subset, average='macro'))
final_score = np.average(scores, weights=[2,1,1])
```

**Submission File**
```
row_id,target
Test_0_consonant_diacritic, 0
Test_0_grapheme_root, 0
Test_0_vowel_diacritic, 0
Test_1_consonant_diacritic, 0
Test_1_grapheme_root, 0
Test_1_vowel_diacritic, 0
...
```

링크: https://www.kaggle.com/competitions/bengaliai-cv19/overview
