# Spanish Controversy Detection Language Model

This repository contains the code of the paper "Anticipating the Debate: Predicting Controversy in News with Transformer-based NLP". 

Controversy is a social phenomenon that emerges when a topic generates large disagreement among people. In the public sphere, controversy is very often related to news. Whereas previous approaches have addressed controversy detection, in this work, we propose to predict controversy based on the title and content of a news post. First, we collect and prepare a dataset from a Spanish news aggregator that labels the news' controversy in a community-based manner. Next, we experiment with the capabilities of language models to learn these labels by fine-tuning models that take both title and content, and the title alone. To cope with data unbalance, we undergo different experiments by sampling the dataset. The best model obtains an 84.72\% micro-F1, trained with an unbalanced dataset and given the title and content as input. The preliminary results show that this task can be learned by relying on linguistic and social features.

## Model 🤖

We use a dataset of news from the Menéame platform, tagged with controversy labels in a community-based manner. The best model was trained with a batch size of 4 and a learning rate of 1e-5 for 5 epochs. We then selected the best checkpoint using the downstream task metric in the corresponding development set and then evaluated it on the test set.

Hugging Face: https://huggingface.co/PlanTL-GOB-ES/Controversy-Prediction

## Dataset 🗂️

<table class="tg" style="undefined;table-layout: fixed; width: 353px">
<colgroup>
<col style="width: 150px">
<col style="width: 124px">
<col style="width: 79px">
</colgroup>
<thead>
  <tr>
    <th class="tg-0pky">Collection</th>
    <th class="tg-0pky">Set</th>
    <th class="tg-0pky">Instances</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" rowspan="2">All</td>
    <td class="tg-0pky">Controversial</td>
    <td class="tg-dvpl">5,584</td>
  </tr>
  <tr>
    <td class="tg-0pky">Non controversial</td>
    <td class="tg-dvpl">231,385</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="3">Unbalanced Subset from All</td>
    <td class="tg-0pky">Train</td>
    <td class="tg-dvpl">18,270</td>
  </tr>
  <tr>
    <td class="tg-0pky">Development</td>
    <td class="tg-dvpl">1,058</td>
  </tr>
  <tr>
    <td class="tg-0pky">Test</td>
    <td class="tg-dvpl">1,058</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="3">Balanced Subset from All</td>
    <td class="tg-0pky">Train</td>
    <td class="tg-dvpl">9,900</td>
  </tr>
  <tr>
    <td class="tg-0pky">Development</td>
    <td class="tg-dvpl">634</td>
  </tr>
  <tr>
    <td class="tg-0pky">Test</td>
    <td class="tg-dvpl">1,058</td>
  </tr>
</tbody>
</table>

## Evaluation ✅
<table style="undefined;table-layout: fixed; width: 437px">
<colgroup>
<col style="width: 107px">
<col style="width: 138px">
<col style="width: 60px">
<col style="width: 68px">
<col style="width: 64px">
</colgroup>
<thead>
  <tr>
    <th>Dataset</th>
    <th>Training Setting</th>
    <th>F1</th>
    <th>Accuracy</th>
    <th>Time (s)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">Balanced</td>
    <td>Title</td>
    <td>0.7026</td>
    <td>0.6295</td>
    <td>1653</td> 
  </tr>
  <tr>
    <td>Title + Summary</td>
    <td>0.8093</td>
    <td>0.7353</td>
    <td>1267</td>
  </tr>
  <tr>
    <td rowspan="2">Unbalanced</td>
    <td>Title</td>
    <td>0.8197</td>
    <td>0.7268</td>
    <td>2631</td>
  </tr>
  <tr>
    <td>Title + Summary</td>
    <td>0.8472</td>
    <td>0.7662</td>
    <td>2615</td>
  </tr>
</tbody>
</table>

## Usage example of the model ⚗️

```
from transformers import pipeline
from pprint import pprint

nlp = pipeline("text-classification", model="PlanTL-GOB-ES/Controversy-Prediction")
example = "Esposas, hijos, nueras y familiares de altos cargos del PP y de la cúpula universitaria llenan la URJC -- Pedro González-Trevijano, rector de la universidad desde 2002 a 2013, ahora magistrado del Tribunal Constitucional, y su sucesor en el cargo, Fernando Suárez han tejido una red que ha dado cobijo laboral a más de un centenar de familiares de vicerrectores, gerentes o catedráticos en los cuatro campus con los que cuenta la universidad localizados en Alcorcón, Móstoles, Fuenlabrada y Vicálvaro."

output = nlp(example)
pprint(output)
```

## Code of our experiments

Dataset transformation: https://github.com/PlanTL-GOB-ES/controversy-detection-model/tree/main/src/dataset

Model training: https://github.com/PlanTL-GOB-ES/controversy-detection-model/tree/main/src/model_training

Statistics and results analysis: https://github.com/PlanTL-GOB-ES/controversy-detection-model/tree/main/src/statistics



## Cite 📣
```
TBA
```

## Contact 📧
For questions regarding this work, contact <bcalvo.bsc@gmail.com>


## Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
