import json
import datasets

logger = datasets.logging.get_logger(__name__)

_CITATION = """ """

_DESCRIPTION = """
               """

_HOMEPAGE = """None"""

_URL = "./split_balanced"
_TRAINING_FILE = "train.json"
_DEV_FILE = "valid.json"
_TEST_FILE = "test.json"


class ControversyConfig(datasets.BuilderConfig):
    """ Builder config for the Controversy dataset """

    def __init__(self, **kwargs):
        """BuilderConfig for Controversy.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(ControversyConfig, self).__init__(**kwargs)


class Controversy(datasets.GeneratorBasedBuilder):
    """ Controversy dataset."""

    BUILDER_CONFIGS = [
        ControversyConfig(
            name="Controversy",
            version=datasets.Version("1.0.0"),
            description="Controversy dataset"
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "sentence": datasets.Value("string"),
                    "label": datasets.features.ClassLabel(
                            names=['CONTROVERSY', 'NO_CONTROVERSY'])
                }
            ),
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls_to_download = {
            "train": f"{_URL}{_TRAINING_FILE}",
            "dev": f"{_URL}{_DEV_FILE}",
            "test": f"{_URL}{_TEST_FILE}",
        }
        downloaded_files = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            for line in f:
                data = json.loads(line)
                sentence = data['title']
                label = 'CONTROVERSY' if data['controversy'] else 'NO_CONTROVERSY'
                yield guid, {
                    "id": str(guid),
                    "sentence": sentence,
                    "label": label
                }
                guid += 1
