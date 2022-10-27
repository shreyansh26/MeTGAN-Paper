# MeTGAN

Code for our work on Memory efficient Tabular GAN for high cardinality categorical datasets.

The source code with the model architecture and the MeTGAN Synthesizer is given in [src/synthesizers/metgan.py](src/synthesizers/metgan.py).

The [data/](data) directory contains the datasets we have used in our work. 

The output files we used in our experiments are in the [syn/](syn) directory.

Check out the [official ICONIP 2021 publication](https://link.springer.com/chapter/10.1007/978-3-030-92310-5_60) or the [unoffical camera-ready version](https://shreyansh26.github.io/files/MeTGAN%20Memory%20Efficient%20Tabular%20GAN%20for%20High%20Cardinality%20Categorical%20Datasets.pdf).

## Dependencies

* Python 3.6+
* Python modules -
    * packaging
    * rdt
    * numpy
    * pandas
    * torch
    * scikit_learn

Exact version information is given in the [requirements.txt](requirements.txt) file.


## Usage

The training code for the various datasets are here -

* [Training on Adult dataset](examples/MeTGAN-Adult.ipynb)
* [Training on the News dataset](examples/MeTGAN-News.ipynb)
* [Training on the Loan dataset](examples/MeTGAN-Loan.ipynb)


## Additional Information

For some of our privacy experiments, we define a set of key columns and sensitive column for the datasets. They are listed here  - 

* **Adult** - 
    * **Key columns** - 'age', 'education-num', 'marital-status', 'race', 'native- country', 'occupation', 'sex', 'hours-per-week'
    * **Sensitive column** - 'income'
    
* **News** - 
    * **Key columns** - 'n_tokens_title', 'n_tokens_content', 'n_unique_tokens', 'data_channel_is_lifestyle', 'data_channel_is_entertainment', 'data_channel_is_bus', 'data_channel_is_socmed', 'data_channel_is_tech', 'weekday_is_monday', 'weekday_is_tuesday', 'weekday_is_wednesday', 'weekday_is_thursday', 'weekday_is_friday', 'weekday_is_saturday', 'weekday_is_sunday', 'is_weekend'
    * **Sensitive column** - 'shares'
    
* **Loan** -
    * **Key columns** -  'State', 'Bank', 'Zip', 'BankState', 'Term', 'UrbanRural', 'BalanceGross', 'ChgOffPrinGr', 'GrAppv'
    * **Sensitive column** - 'SBA_Appv'


## Credits

Huge credits to the [official CTGAN repository](https://github.com/sdv-dev/CTGAN) on which we base most of our code.

## Citation

```
@InProceedings{10.1007/978-3-030-92310-5_60,
    author="Singh, Shreyansh
    and Kayathwal, Kanishka
    and Wadhwa, Hardik
    and Dhama, Gaurav",
    editor="Mantoro, Teddy
    and Lee, Minho
    and Ayu, Media Anugerah
    and Wong, Kok Wai
    and Hidayanto, Achmad Nizar",
    title="MeTGAN: Memory Efficient Tabular GAN for High Cardinality Categorical Datasets",
    booktitle="Neural Information Processing",
    year="2021",
    publisher="Springer International Publishing",
    address="Cham",
    pages="519--527",
    isbn="978-3-030-92310-5"
}
```