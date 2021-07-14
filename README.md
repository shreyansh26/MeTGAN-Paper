# MeTGAN

Code (currently private) + Additional Information for our work on Memory efficient Tabular GAN for high cardinality categorical datasets.

The [data/](data) directory contains the datasets we have used in our work. 


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

