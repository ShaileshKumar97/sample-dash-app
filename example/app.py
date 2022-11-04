from explainit.app import build
import pandas as pd

ref_data = pd.read_csv("https://raw.githubusercontent.com/katonic-dev/explainit/master/examples/data/reference_data.csv", index_col=None)
prod_data = pd.read_csv("https://raw.githubusercontent.com/katonic-dev/explainit/master/examples/data/production_data.csv", index_col=None)

build(
  reference_data=ref_data,
  production_data=prod_data,
  target_col_name="bad_loan",
  target_col_type="cat",
  host="127.0.0.1",
  port=8050
)