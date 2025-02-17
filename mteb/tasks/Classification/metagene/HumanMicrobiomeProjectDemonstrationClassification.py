from __future__ import annotations

from mteb.abstasks.AbsTaskClassification import AbsTaskClassification
from mteb.abstasks.TaskMetadata import TaskMetadata


class HumanMicrobiomeProjectDemonstrationClassificationDisease(AbsTaskClassification):
    metadata = TaskMetadata(
        name="HumanMicrobiomeProjectDemonstrationClassificationDisease",
        description="A Classification task for predicting the disease from the Human Microbiome Project Demonstration dataset.",
        reference="https://huggingface.co/datasets/metagene-ai/HumanMicrobiomeProjectDemonstration/tree/main/hmpd/disease",
        dataset={
            "path": "metagene-ai/HumanMicrobiomeProjectDemonstration",
            "name": "disease",
            "revision": "main",
        },
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng"],
        main_score="accuracy",
        date=("2009-10-09", "2012-11-22"),
        domains=["Medical"],
        task_subtypes=None,
        license="not specified",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""
        @article{liu2025metagene,
            title={METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring},
            author={Liu, Ollie and Jaghouar, Sami and Hagemann, Johannes and Wang, Shangshang and Wiemels, Jason and Kaufman, Jeff and Neiswanger, Willie},
            journal={arXiv preprint arXiv:2501.02045},
            year={2025}
        }
        """
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method = "logReg"

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        from transformers.trainer_utils import set_seed
        set_seed(42)

        import datasets

        self.dataset = datasets.load_dataset(**self.metadata_dict["dataset"])  # type: ignore

        self.dataset_transform()

        full_train_dataset = self.dataset['train']

        # by default, we undersample the training data to 8 samples per label
        desired_train_samples = 8

        from collections import Counter
        label_counts = Counter(full_train_dataset['label'])
        M = min(label_counts.values())
        if M < desired_train_samples:
            raise ValueError(
                f"Not enough samples per label to achieve {desired_train_samples} "
                f"training samples. The smallest label has only {M} samples."
            )
        test_size = 1 - (desired_train_samples / M)
        split_datasets = full_train_dataset.train_test_split(
            test_size=test_size,
            shuffle=True,
            seed=42)
        new_train_dataset = split_datasets['train']
        new_test_dataset = split_datasets['test']
        self.dataset = datasets.DatasetDict({
            'train': new_train_dataset,
            'test': new_test_dataset
        })
        print(f"\nSplitting the data with test_size={test_size}")
        print(f"Train set size: {len(new_train_dataset)} rows")
        print(f"Test set size: {len(new_test_dataset)} rows\n")

        self.data_loaded = True

    def dataset_transform(self):
        self.dataset = self.dataset.rename_columns({"sequence": "text", "disease": "label"})


class HumanMicrobiomeProjectDemonstrationClassificationSex(AbsTaskClassification):
    metadata = TaskMetadata(
        name="HumanMicrobiomeProjectDemonstrationClassificationSex",
        description="A Classification task for predicting the sex from the Human Microbiome Project Demonstration dataset.",
        reference="https://huggingface.co/datasets/metagene-ai/HumanMicrobiomeProjectDemonstration/tree/main/hmpd/sex",
        dataset={
            "path": "metagene-ai/HumanMicrobiomeProjectDemonstration",
            "name": "sex",
            "revision": "main",
        },
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng"],
        main_score="accuracy",
        date=("2009-10-09", "2012-11-22"),
        domains=["Medical"],
        task_subtypes=None,
        license="not specified",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""
        @article{liu2025metagene,
            title={METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring},
            author={Liu, Ollie and Jaghouar, Sami and Hagemann, Johannes and Wang, Shangshang and Wiemels, Jason and Kaufman, Jeff and Neiswanger, Willie},
            journal={arXiv preprint arXiv:2501.02045},
            year={2025}
        }
        """
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method = "logReg"

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        from transformers.trainer_utils import set_seed
        set_seed(42)

        import datasets
        self.dataset = datasets.load_dataset(**self.metadata_dict["dataset"])  # type: ignore

        self.dataset_transform()

        full_train_dataset = self.dataset['train']

        # by default, we undersample the training data to 8 samples per label
        desired_train_samples = 8

        from collections import Counter
        label_counts = Counter(full_train_dataset['label'])
        M = min(label_counts.values())
        if M < desired_train_samples:
            raise ValueError(
                f"Not enough samples per label to achieve {desired_train_samples} "
                f"training samples. The smallest label has only {M} samples."
            )
        test_size = 1 - (desired_train_samples / M)
        split_datasets = full_train_dataset.train_test_split(
            test_size=test_size,
            shuffle=True,
            seed=42)
        new_train_dataset = split_datasets['train']
        new_test_dataset = split_datasets['test']
        self.dataset = datasets.DatasetDict({
            'train': new_train_dataset,
            'test': new_test_dataset
        })
        print(f"\nSplitting the data with test_size={test_size}")
        print(f"Train set size: {len(new_train_dataset)} rows")
        print(f"Test set size: {len(new_test_dataset)} rows\n")

        self.data_loaded = True

    def dataset_transform(self):
        self.dataset = self.dataset.rename_columns({"sequence": "text", "host_sex": "label"})


class HumanMicrobiomeProjectDemonstrationClassificationSource(AbsTaskClassification):
    metadata = TaskMetadata(
        name="HumanMicrobiomeProjectDemonstrationClassificationSource",
        description="A Classification task for predicting the source from the Human Microbiome Project Demonstration dataset.",
        reference="https://huggingface.co/datasets/metagene-ai/HumanMicrobiomeProjectDemonstration/tree/main/hmpd/source",
        dataset={
            "path": "metagene-ai/HumanMicrobiomeProjectDemonstration",
            "name": "source",
            "revision": "main",
        },
        type="Classification",
        category="s2s",
        modalities=["text"],
        eval_splits=["test"],
        eval_langs=["eng"],
        main_score="accuracy",
        date=("2009-10-09", "2012-11-22"),
        domains=["Medical"],
        task_subtypes=None,
        license="not specified",
        annotations_creators="derived",
        dialect=[],
        sample_creation="found",
        bibtex_citation="""
        @article{liu2025metagene,
            title={METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring},
            author={Liu, Ollie and Jaghouar, Sami and Hagemann, Johannes and Wang, Shangshang and Wiemels, Jason and Kaufman, Jeff and Neiswanger, Willie},
            journal={arXiv preprint arXiv:2501.02045},
            year={2025}
        }
        """
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.method = "logReg"

    def load_data(self, **kwargs):
        if self.data_loaded:
            return

        from transformers.trainer_utils import set_seed
        set_seed(42)

        import datasets
        self.dataset = datasets.load_dataset(**self.metadata_dict["dataset"])  # type: ignore

        self.dataset_transform()

        full_train_dataset = self.dataset['train']

        # by default, we undersample the training data to 8 samples per label
        desired_train_samples = 8

        from collections import Counter
        label_counts = Counter(full_train_dataset['label'])
        M = min(label_counts.values())
        if M < desired_train_samples:
            raise ValueError(
                f"Not enough samples per label to achieve {desired_train_samples} "
                f"training samples. The smallest label has only {M} samples."
            )
        test_size = 1 - (desired_train_samples / M)
        split_datasets = full_train_dataset.train_test_split(
            test_size=test_size,
            shuffle=True,
            seed=42)
        new_train_dataset = split_datasets['train']
        new_test_dataset = split_datasets['test']
        self.dataset = datasets.DatasetDict({
            'train': new_train_dataset,
            'test': new_test_dataset
        })
        print(f"\nSplitting the data with test_size={test_size}")
        print(f"Train set size: {len(new_train_dataset)} rows")
        print(f"Test set size: {len(new_test_dataset)} rows\n")

        self.data_loaded = True

    def dataset_transform(self):
        self.dataset = self.dataset.rename_columns({"sequence": "text", "isolation_source": "label"})