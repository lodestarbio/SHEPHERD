from pathlib import Path


#PROJECT_DIR = Path("/home/ema30/zaklab/rare_disease_dx/test_camera_ready") # Path('PATH/TO/SHEPHERD')
PROJECT_DIR = Path("/opt/app") # Path('PATH/TO/SHEPHERD')
CURR_KG = '8.9.21_kg'
DATA_PATH = Path("/data")
KG_DIR = DATA_PATH / 'knowledge_graph' / CURR_KG
PREDICT_RESULTS_DIR =  DATA_PATH / 'results'
SEED = 33

# Modify the following variables for your dataset
MY_DATA_DIR = DATA_PATH / "patients/simulated_patients"
MY_TRAIN_DATA = MY_DATA_DIR / f"disease_split_train_sim_patients_{CURR_KG}.txt"
MY_VAL_DATA = MY_DATA_DIR / f"disease_split_val_sim_patients_{CURR_KG}.txt"
# MY_TEST_DATA = ?

# not sure what these are
CORRUPT_TRAIN_DATA = MY_DATA_DIR / f"disease_split_train_sim_patients_{CURR_KG}_phencorrupt.txt"
CORRUPT_VAL_DATA = MY_DATA_DIR / f"disease_split_val_sim_patients_{CURR_KG}_phencorrupt.txt"

#MY_TRAIN_DATA = MY_DATA_DIR / f"disease_split_all_sim_patients_{CURR_KG}.txt"
#MY_VAL_DATA = "/n/data1/hms/dbmi/zaklab/mli/rare_disease_diagnosis/test_camera_ready/data/patients/mygene2_patients/mygene2_5.7.22.txt"

#MY_TEST_DATA = "/n/data1/hms/dbmi/zaklab/mli/rare_disease_diagnosis/test_camera_ready/data/patients/simulated_patients/all_simulated_ddd_mygene2_5.7.22_max20candgenes_phencorrupt.txt"

# Exomiser
# MY_TEST_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_exomiser_distractor_genes_5_candidates_mapped_only_genes.txt" # MY_DATA_DIR / "PATH/TO/YOUR/DATA"
# MY_SPL_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_exomiser_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_matrix.npy" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_matrix.npy)
# MY_SPL_INDEX_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_exomiser_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_index_dict.pkl" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_index_dict.pkl)

# Curated
#MY_TEST_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_manual_baylor_nobgm_distractor_genes_5_candidates_mapped_only_genes.txt" # MY_DATA_DIR / "PATH/TO/YOUR/DATA"
#MY_SPL_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_manual_baylor_nobgm_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_matrix.npy" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_matrix.npy)
#MY_SPL_INDEX_DATA = "/home/ema30/zaklab/rare_disease_dx/formatted_patients/UDN_patients-2022-01-05/all_udn_patients_kg_8.9.21_kgsolved_manual_baylor_nobgm_distractor_genes_5_candidates_mapped_only_genes_agg=mean_spl_index_dict.pkl" #MY_DATA_DIR / "PATH/TO/YOUR/DATA" # Result of data_prep/shortest_paths/add_spl_to_patients.py (suffix: _spl_index_dict.pkl)
