# Spanish Controversy Detection Language Model

TBA

## Model 🤖
- TBA

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
    <td class="tg-dvpl">18,000</td>
  </tr>
  <tr>
    <td class="tg-0pky">Development</td>
    <td class="tg-dvpl">1,000</td>
  </tr>
  <tr>
    <td class="tg-0pky">Test</td>
    <td class="tg-dvpl">1,386</td>
  </tr>
  <tr>
    <td class="tg-0pky" rowspan="3">Balanced Subset from All</td>
    <td class="tg-0pky">Train</td>
    <td class="tg-dvpl">9,990</td>
  </tr>
  <tr>
    <td class="tg-0pky">Development</td>
    <td class="tg-dvpl">589</td>
  </tr>
  <tr>
    <td class="tg-0pky">Test</td>
    <td class="tg-dvpl">589</td>
  </tr>
</tbody>
</table>

- Zenodo: TBA
- HuggingFace: TBA

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
    <td>0.6536</td>
    <td>0.6689</td>
    <td>817</td>
  </tr>
  <tr>
    <td>Title + Summary</td>
    <td>0.6666</td>
    <td>0.6740</td>
    <td>841</td>
  </tr>
  <tr>
    <td rowspan="2">Unbalanced</td>
    <td>Title</td>
    <td>0.8331</td>
    <td>0.7532</td>
    <td>1472</td>
  </tr>
  <tr>
    <td>Title + Summary</td>
    <td>0.8584</td>
    <td>0.7712</td>
    <td>1425</td>
  </tr>
</tbody>
</table>

## Usage example ⚗️
```
TBA
```

## Other Spanish Language Models 👩‍👧‍👦
We are developing general domain and domain-specific language models:
- 💃🏻  [General domain](https://github.com/PlanTL-GOB-ES/lm-spanish)
- ⚖️ [Legal Language Model](https://github.com/PlanTL-GOB-ES/lm-legal-es)
- ⚕️ [Biomedical and Clinical Language Models](https://github.com/PlanTL-GOB-ES/lm-biomedical-clinical-es) 

## Cite 📣
```
TBA
```

## Contact 📧
📋 We are interested in (1) extending our corpora to make larger models (2) train/evaluate the model in other tasks.

For questions regarding this work, contact <plantl-gob-es@bsc.es>


## Disclaimer

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of artificial intelligence.

In no event shall the owner of the models (SEDIA – State Secretariat for digitalization and artificial intelligence) nor the creator (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.


Los modelos publicados en este repositorio tienen una finalidad generalista y están a disposición de terceros. Estos modelos pueden tener sesgos y/u otro tipo de distorsiones indeseables.

Cuando terceros desplieguen o proporcionen sistemas y/o servicios a otras partes usando alguno de estos modelos (o utilizando sistemas basados en estos modelos) o se conviertan en usuarios de los modelos, deben tener en cuenta que es su responsabilidad mitigar los riesgos derivados de su uso y, en todo caso, cumplir con la normativa aplicable, incluyendo la normativa en materia de uso de inteligencia artificial.

En ningún caso el propietario de los modelos (SEDIA – Secretaría de Estado de Digitalización e Inteligencia Artificial) ni el creador (BSC – Barcelona Supercomputing Center) serán responsables de los resultados derivados del uso que hagan terceros de estos modelos.
