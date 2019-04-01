[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/fadymedhat/UrbanSound8K-for-MCLNN/blob/master/LICENSE)

# UrbanSound8K dataset for MCLNN

The [UrbanSound8k](https://urbansounddataset.weebly.com/urbansound8k.html) environmental sound dataset.

| Clip Duration  | Format | Count | Categories|
|:---:|:---:|:---:|:---:|
| max 4 secs | .wav | 8732 | 10 |

Dataset Summary:
 * clips have a maximum of 4-seconds length with different sampling rates.
 * dataset is released into predefined 10-fold splits for cross-validation.

 
 This folder contains:
  * Scripts required to prepare the UrbanSound8k dataset for the MCLNN processing.
  * Pretrained weights and indices for the 10-fold cross-validation in addition to the standardization parameters 
  to replicate the results in:
 
    _Fady Medhat, David Chesmore and John Robinson, "Recognition of Acoustic Events Using Masked Conditional Neural Networks," 2017 16th IEEE International Conference on Machine Learning and Applications (ICMLA)_
 
 ## Prepossessing
 
The following are the steps involved in preparing the UrbanSound8k dataset:
1) Unify the samplying rate.
2) Clone and concatenate each sample to make its length at least equal to 4 seconds.
3) Redistribute the 10-folds folders to a folder per category.

#### Preparation scripts prerequisites

The [preparation scripts](https://github.com/fadymedhat/UrbanSound8K-for-MCLNN/tree/master/UrbanSound8K_preparation_scripts) require the following packages to be installed beforehand:
   * [ffmpeg](https://www.ffmpeg.org/) version N-81489-ga37e6dd
   * numpy 1.11.2+mkl
   * librosa 0.4.0
   * h5py 2.6.0
 
#### Steps
1. Download the dataset and execute the scripts in the [preparation scripts](https://github.com/fadymedhat/UrbanSound8K-for-MCLNN/tree/master/UrbanSound8K_preparation_scripts) following the order of their labels.
2. Make sure the files are ordered following the [UrbanSound8K_storage_ordering](https://github.com/fadymedhat/UrbanSound8K-for-MCLNN/blob/master/UrbanSound8K_storage_ordering.txt) file.
3. Configure the spectrogram transformation within the [Dataset Transformer](https://github.com/fadymedhat/MCLNN/tree/master/dataset_transformer) and generate the MCLNN-Ready hdf5 for the dataset using the [Urbansound8k_MCLNN.csv](https://github.com/fadymedhat/Urbansound8K-for-MCLNN/blob/master/UrbanSound8K_preparation_scripts/UrbanSound8KwithAdditionalColumnsForMCLNN.csv)  file.
4. Generate the indices for the folds using the [Index Generator](https://github.com/fadymedhat/MCLNN/tree/master/index_generator) script.
