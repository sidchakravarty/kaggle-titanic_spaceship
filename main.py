from kaggle import Kaggle as k

if __name__ == '__main__':
    # Use this to initiate the Kaggle Competition dataset
   data = k("kaggle datasets download -d defcodeking/spaceship-titanic-prepared-datasets")

   for _ in data.dataset:
       print(_)
