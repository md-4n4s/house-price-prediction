from . import INPUT_PATH, clean_data, load_data


def main():
    df = load_data(INPUT_PATH, index_col="Order")

    # Columns are grouped based on their requirement for filling missing values
    MISSING_VALUE_STRATEGY = {
        "mean": ["lot_frontage"],
        "none": [
            "alley",
            "mas_vnr_type",
            "bsmt_qual",
            "bsmt_cond",
            "bsmtfin_type_1",
            "bsmtfin_type_2",
            "electrical",
            "fireplace_qu",
            "garage_type",
            "garage_finish",
            "garage_qual",
            "garage_cond",
            "pool_qc",
            "fence",
            "misc_feature",
        ],
        "zero": [
            "mas_vnr_area",
            "bsmtfin_sf_1",
            "bsmtfin_sf_2",
            "bsmt_unf_sf",
            "total_bsmt_sf",
            "bsmt_full_bath",
            "bsmt_half_bath",
            "garage_yr_blt",
            "garage_cars",
            "garage_area",
        ],
        "mode": ["bsmt_exposure"],
    }

    df = clean_data(df, MISSING_VALUE_STRATEGY, ["unnamed:_0"])

    return df


if __name__ == "__main__":
    main()
