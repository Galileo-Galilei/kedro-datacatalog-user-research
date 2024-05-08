# kedro-datacatalog-user-research

A repo with examples of how I use Kedro's DataCatalog for user research interview


## Use case 1 : DataCatalog for data analytics

I train data analysts to produce more reproducible analysis. I mostly use the [Supercharge your data science notebook with Kedro](https://kedro.org/blog/add-kedro-to-your-data-science-notebook) blog post to introduce them to Kedro, and mostly focus on the ``DataCatalog`` and the ``Dataset`` concepts as standalone components. The configloader is not indtroduced, I jUSt give them a template to put to the beginning of their script. 

```{note}
I will use a python script instead of a notebook for ease of versioning here, but most of the developments are made in a notebook.  
```

Funnily, the use of the catalog through code is considered "advanced use" in kedro documentation.  

### API used**: 
- ``catalog.load()``
- ``catalog.save(data)``

### Most common issues**: 

####Confusion with ``DataSet`` and ``Dataset``

They have been renamed in 0.19, and the blog post still uses the old convention? Since these users have no kedro knowledge and sometimes little python knowledge, this is hard to debug for them:

```bash
DatasetError: An exception occurred when parsing config for dataset 'companies':
Class 'pandas.CSVDataSet' not found, is this a typo?
```

#### Hard to debug and confusing error message if the yaml is invalid 

If they have an invalid entry in their ``catalog.yml``, they got a very confusing error message like ``AttributeError: 'str' object has no attribute 'items'``

![alt text](image.png)

#### Unclear error message when kedro-datasets is not installed 

```bash
DatasetError: An exception occurred when parsing config for dataset 'companies':
Class 'pandas.CSVDataset' not found, is this a typo?
```

The root cause here is ``kedro-datasets`` not being installed, but the error message could be more explicit. 

#### No lazy loading forces to install the entire requirements suite

If I install ``kedro-datasets``, I now get the following error message: 

```bash
DatasetError: An exception occurred when parsing config for dataset 'companies':
No module named 'pandas'. Please see the documentation on how to install relevant dependencies for kedro_datasets.pandas.CSVDataset:
```

When they have a lot of data entries and different dependencies and they just want to rerun partially an anaysis, they are sometimes frustrated because they need to install all packages to just load one data source, and they don't have all the proper requirements: why would I need to install excel dependencies to instantiate the ``DataCatalog`` to load a csv which does not need Excel?

#### Difficulty to know how to configure the dataset

They tend do not not know the underlying library to the datasets. They need to be redirected to the right place in the documentation (e.g. [pandas.CSVDataset API doc](https://docs.kedro.org/projects/kedro-datasets/en/kedro-datasets-3.0.0/api/kedro_datasets.pandas.CSVDataset.html))

#### Hard to find the dataset they want

When they have a lot of catalog entries which sis common because they tend to store a lot of intermediate results), they go back and forth with the yaml file to find how they named the dataset. They'd like :
   - autocomplete
   - pretty printing (``print(catalog)`` should give something understandable than a long, *a minima* ``catalog.list()`` and maybe details on the dataset)
   - ability to search datasets, something like ``catalog.search(regex="es$") # output: ["companies", "shuttles"]`` )


#### Credentials

How credentials works are hard to grasp, but this is out of scope here.  

