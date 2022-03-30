# Bengali AI Handwritten Grapheme Classification
> 이유한님의 유튜브를 보면서 공부한 내용들을 정리

## Overview
벵골어는 수억명의 사용자를 가진 세계에서 다섯 번째로 많이 사용되는 언어이다. 방글라데시의 공용어이고, 인도에서 두 번째로 많이 사용되는 언어이다. 그 범위를 고려해봤을 때, 손으로 쓴 언어의 이미지를 광학적으로 인식할 수 있는 AI를 개발하는 데에 사업적, 교육적으로 상당한 관심이 있다.

광학 문자 인식은 벵골어에게 있어 특히 어렵다. 벵골어는 49개의 글자(모음: 11개, 자음: 38개)를 가지고 있지만, 18개의 잠재적인 억양이 있다. 이것은 가장 작은 단위인 문자소(grapheme)가 많다는 것을 의미한다. 더해진 복잡성은 최대 13000개의 문자소 변형이 발생한다.(영어의 경우 250개의 graphemic units)

이 대회에서는 손으로 쓴 벵골어 문자 이미지가 제공된다. 이미지에서 세 가지 구성 요소(grapheme root, vowel diacritics and consonant diacritics)를 개별적으로 분류해야 한다.

링크: https://www.kaggle.com/competitions/bengaliai-cv19/overview
