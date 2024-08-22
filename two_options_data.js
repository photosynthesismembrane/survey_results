const image_data = [
    {
        "image_filename": "6c21114880937e39b4bea10ce45567c2.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b81f8506ba3431e9fbc8c0d74b93b61e.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "a67ca6813835e5e58961d4336e46c197.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b129f69309638fda34b7da2ebbfce83a.jpg",
        "question": "balance_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "437f14c6a2218e91d70e2ed77a05ee36.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "9fab78a3b8c1e0126dcc943baee8918d.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "lorenzo-lotto_christ-s-farewell-to-mary-1521.jpg",
        "question": "proportion",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_departure-of-christ-from-mary-with-mary-and-martha-the-sisters-of-lazarus-1518.jpg",
        "question": "proportion",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giovanni-antonio-boltraffio_portrait-alleged-to-be-of-anne-whateley-in-fact-likely-to-be-girolamo-casio-1495.jpg",
        "question": "proportion",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_st-peter-enthroned-with-saints.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-transfiguration-1520.jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_the-adoration-of-the-magi-1518(2).jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "437f14c6a2218e91d70e2ed77a05ee36.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "fe52baad9432a25851278bfa7ec3a86f.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0ed30ccd0baf1c1332e6e082c64455a4.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d792700abadc24170124b8b01915d5f8.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "a25602e9ef1dc788c586c70081a442f2.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "e8cad5095d378494dcfc41b2d33d8915.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "437f14c6a2218e91d70e2ed77a05ee36.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "fe52baad9432a25851278bfa7ec3a86f.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "1eb250ac61e9ffca969c5f528ead6b23.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "26c521930dd73c0bf8a8675b08698b51.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0cfe6cbc00ffd9c46c5ca805eedb14a5.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "vittore-carpaccio_arrival-of-st-ursula-during-the-siege-of-cologne-1498.jpg",
        "question": "contrast_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_the-adoration-of-the-magi-1518(2).jpg",
        "question": "contrast_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_st-peter-enthroned-with-saints.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_altar-polyptych-of-san-bartolomeo-bergamo-foot-plate-entombment-1516.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-repatriation-of-the-english-ambassadors-1500.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cb5b90942c93eb6688aaa0b633df56a9.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "1eb250ac61e9ffca969c5f528ead6b23.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "437f14c6a2218e91d70e2ed77a05ee36.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "233d54e476efa149bbd2ceedd1656fcf.jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "fe4c7983efd3242e7322ecee9c665e68.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "andrea-mantegna_st-jacques-leads-to-martyrdom.jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_the-healing-of-anianus.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_departure-of-christ-from-mary-with-mary-and-martha-the-sisters-of-lazarus-1518.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_musical-instruments-music-1510(1).jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_marriage-of-the-virgin-1504.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-miracle-of-the-relic-of-the-true-cross-on-the-rialto-bridge-1494.jpg",
        "question": "balance_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_the-sunset-1510(1).jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_four-saints-from-left-st-peter-st-martha-st-mary-magdalene-st-leonard-1517.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_adoration-of-the-christ-child(2).jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-blinding-of-elymas-cartoon-for-the-sistine-chapel.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_the-annunciation-1513.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_marriage-of-the-virgin-1504.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_four-saints-from-left-st-peter-st-martha-st-mary-magdalene-st-leonard-1517.jpg",
        "question": "proportion",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-virgin-reading-1510.jpg",
        "question": "proportion",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_the-vision-of-st-bernard.jpg",
        "question": "proportion",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_samson-and-delilah-1506.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-departure-of-the-english-ambassadors-1498.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "0875a6148f7da92df0fc6a258bf00c77.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "6c21114880937e39b4bea10ce45567c2.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "2174b333c91d2fa7d936e97e4386d983.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "a25602e9ef1dc788c586c70081a442f2.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b0c8ad1947f1a30d4d746c963696f4ce.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "9fab78a3b8c1e0126dcc943baee8918d.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "317cbd7af35213a4a80e5d31e30368e8.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "8b2e6c3080203d4d1badfa56b753a6d3.jpg",
        "question": "eye_movement_2",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "fe52baad9432a25851278bfa7ec3a86f.jpg",
        "question": "eye_movement_2",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "dd5d1b60db599be5e8c238bee8462a15.jpg",
        "question": "eye_movement_2",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "233d54e476efa149bbd2ceedd1656fcf.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "6c21114880937e39b4bea10ce45567c2.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0875a6148f7da92df0fc6a258bf00c77.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "7a566e1c05c0b42c118760aeecc47edb.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d792700abadc24170124b8b01915d5f8.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0cfe6cbc00ffd9c46c5ca805eedb14a5.jpg",
        "question": "balance_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "raphael_the-marriage-of-the-virgin-1504-1.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_isaac-and-rebecca-spied-upon-by-abimelech-1519.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_the-annunciation-1513.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_samson-and-delilah-1506.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-death-of-ananias-cartoon-for-the-sistine-chapel.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-departure-of-the-english-ambassadors-1498.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "6c21114880937e39b4bea10ce45567c2.jpg",
        "question": "contrast_elements",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0ed30ccd0baf1c1332e6e082c64455a4.jpg",
        "question": "contrast_elements",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "2174b333c91d2fa7d936e97e4386d983.jpg",
        "question": "contrast_elements",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "39a2d1a7508ac84e097b717704ede66e.jpg",
        "question": "composition",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d8c5f661e9d5ffa8bffc814a3fc6e935.jpg",
        "question": "composition",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "7a566e1c05c0b42c118760aeecc47edb.jpg",
        "question": "composition",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph-1.jpg",
        "question": "foreground_background_4",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_four-saints-from-left-st-peter-st-martha-st-mary-magdalene-st-leonard-1517.jpg",
        "question": "foreground_background_4",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_captured-statues-and-siege-equipment-1506.jpg",
        "question": "foreground_background_4",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-martyrdom-of-st-jacques.jpg",
        "question": "focus_point",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-miracle-of-the-relic-of-the-true-cross-on-the-rialto-bridge-1494.jpg",
        "question": "focus_point",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "focus_point",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "9ecc59478f04350c181bb99b75a1e6c4.jpg",
        "question": "eye_movement_2",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0875a6148f7da92df0fc6a258bf00c77.jpg",
        "question": "eye_movement_2",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "eye_movement_2",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "e2e69c417d307e48ed275826300dacbd.jpg",
        "question": "balance_elements",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "1c501095b675902362f6e9dcc8bab246.jpg",
        "question": "balance_elements",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "39a2d1a7508ac84e097b717704ede66e.jpg",
        "question": "balance_elements",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "vittore-carpaccio_the-repatriation-of-the-english-ambassadors-1500.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-martyrdom-of-st-jacques.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_altar-of-st-lucia-st-lucia-in-front-of-the-judges-1532.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph-1.jpg",
        "question": "focus_point",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-virgin-reading-1510.jpg",
        "question": "focus_point",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_the-sunset-1510(1).jpg",
        "question": "focus_point",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "39a2d1a7508ac84e097b717704ede66e.jpg",
        "question": "balance_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0ed30ccd0baf1c1332e6e082c64455a4.jpg",
        "question": "balance_elements",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "e2e69c417d307e48ed275826300dacbd.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "9ecc59478f04350c181bb99b75a1e6c4.jpg",
        "question": "eye_movement_2",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "1eb250ac61e9ffca969c5f528ead6b23.jpg",
        "question": "eye_movement_2",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "a67ca6813835e5e58961d4336e46c197.jpg",
        "question": "balance_elements",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "24c5eda44962442b432db52c7dfd5d1a.jpg",
        "question": "balance_elements",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "1c501095b675902362f6e9dcc8bab246.jpg",
        "question": "balance_elements",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d8c5f661e9d5ffa8bffc814a3fc6e935.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "7a566e1c05c0b42c118760aeecc47edb.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d64d133d79b7ad425c6f52a8e02a09f5.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "raphael_the-death-of-ananias-cartoon-for-the-sistine-chapel.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-marriage-of-the-virgin-1504-1.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_the-annunciation-1513.jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-glory-of-st-vidal-1514.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_st-jacques-leads-to-martyrdom.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "renaissance"
    },
    {
        "image_filename": "26c521930dd73c0bf8a8675b08698b51.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "f78e6b6a97e7c5bb2d9b77952e43b428.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b129f69309638fda34b7da2ebbfce83a.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "0cfe6cbc00ffd9c46c5ca805eedb14a5.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "cogvlm",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "9ecc59478f04350c181bb99b75a1e6c4.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "llava",
        "contestant_2": "cogvlm",
        "data_type": "pinterest"
    },
    {
        "image_filename": "437f14c6a2218e91d70e2ed77a05ee36.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "llava",
        "contestant_2": "deepseek",
        "data_type": "pinterest"
    },
    {
        "image_filename": "6c21114880937e39b4bea10ce45567c2.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "2174b333c91d2fa7d936e97e4386d983.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "1eb250ac61e9ffca969c5f528ead6b23.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b129f69309638fda34b7da2ebbfce83a.jpg",
        "question": "contrast_elements",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "178acaa395581f4c77c1510a253e3ced.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "26c521930dd73c0bf8a8675b08698b51.jpg",
        "question": "contrast_elements",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "andrea-mantegna_the-martyrdom-of-st-jacques.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-agony-in-the-garden.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_marriage-of-the-virgin-1504.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_the-healing-of-anianus.jpg",
        "question": "focus_point",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_isaac-and-rebecca-spied-upon-by-abimelech-1519.jpg",
        "question": "focus_point",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-repatriation-of-the-english-ambassadors-1500.jpg",
        "question": "focus_point",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_departure-of-christ-from-mary-with-mary-and-martha-the-sisters-of-lazarus-1518.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_christ-s-farewell-to-mary-1521.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "dosso-dossi_the-three-ages-of-man-1515.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_pala-di-corciano-annunciation.jpg",
        "question": "foreground_background_4",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-blinding-of-elymas-cartoon-for-the-sistine-chapel.jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_musical-instruments-music-1510(1).jpg",
        "question": "foreground_background_4",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "e8cad5095d378494dcfc41b2d33d8915.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "fe4c7983efd3242e7322ecee9c665e68.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d8c5f661e9d5ffa8bffc814a3fc6e935.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "cb5b90942c93eb6688aaa0b633df56a9.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "4dceb2db532d3e56bfadf5b1a28713c2.jpg",
        "question": "foreground_background_4",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "317cbd7af35213a4a80e5d31e30368e8.jpg",
        "question": "foreground_background_4",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "dd5d1b60db599be5e8c238bee8462a15.jpg",
        "question": "focus_point",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "9ecc59478f04350c181bb99b75a1e6c4.jpg",
        "question": "focus_point",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "7a566e1c05c0b42c118760aeecc47edb.jpg",
        "question": "focus_point",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "e2e69c417d307e48ed275826300dacbd.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "b3de88d2fa3fbf442749bcbf10bb8939.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "d792700abadc24170124b8b01915d5f8.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "pinterest"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph.jpg",
        "question": "focus_point",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_the-annunciation-1513.jpg",
        "question": "focus_point",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-repatriation-of-the-english-ambassadors-1500.jpg",
        "question": "focus_point",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-marriage-of-the-virgin-1504-1.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-agony-in-the-garden.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-martyrdom-of-st-jacques.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_pala-di-fano-nativity-of-mary.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph-1.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph.jpg",
        "question": "eye_movement_2",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-departure-of-the-english-ambassadors-1498.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_st-cecilia-with-saints-detail-1516-1.jpg",
        "question": "eye_movement_2",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-agony-in-the-garden.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-miracle-of-the-relic-of-the-true-cross-on-the-rialto-bridge-1494.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_the-sunset-1510(1).jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_pala-di-fano-nativity-of-mary.jpg",
        "question": "proportion",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_altar-of-st-lucia-st-lucia-in-front-of-the-judges-1532.jpg",
        "question": "proportion",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_st-cecilia-with-saints-detail-1516-1.jpg",
        "question": "proportion",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_pala-di-fano-nativity-of-mary.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-marriage-of-the-virgin-1504-1.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_the-glory-of-st-vidal-1514.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_departure-of-christ-from-mary-with-mary-and-martha-the-sisters-of-lazarus-1518.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-agony-in-the-garden.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_isaac-and-rebecca-spied-upon-by-abimelech-1519.jpg",
        "question": "balance_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-death-of-ananias-cartoon-for-the-sistine-chapel.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_the-healing-of-anianus.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_captured-statues-and-siege-equipment-1506.jpg",
        "question": "composition",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_st-peter-enthroned-with-saints.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_altar-polyptych-of-san-bartolomeo-bergamo-foot-plate-entombment-1516.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_the-adoration-of-the-magi-1518(2).jpg",
        "question": "foreground_background_4",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_samson-and-delilah-1506.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_st-peter-enthroned-with-saints.jpg",
        "question": "composition",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_four-saints-from-left-st-peter-st-martha-st-mary-magdalene-st-leonard-1517.jpg",
        "question": "composition",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_the-annunciation-1513.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-guards-outside-the-prison-detail-from-the-liberation-of-st-peter-in-the-stanza-d-eliodoro-1514.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_adoration-of-the-christ-child(2).jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_the-sunset-1510(1).jpg",
        "question": "focus_point",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_captured-statues-and-siege-equipment-1506.jpg",
        "question": "focus_point",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giovanni-antonio-boltraffio_portrait-alleged-to-be-of-anne-whateley-in-fact-likely-to-be-girolamo-casio-1495.jpg",
        "question": "focus_point",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "contrast_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-marriage-of-the-virgin-1504-1.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_pala-di-fano-nativity-of-mary.jpg",
        "question": "contrast_elements",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_altar-polyptych-of-san-bartolomeo-bergamo-foot-plate-entombment-1516.jpg",
        "question": "proportion",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph.jpg",
        "question": "proportion",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "vittore-carpaccio_virgin-mary-and-john-the-baptist-praying-to-the-child-christ.jpg",
        "question": "proportion",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "dosso-dossi_the-three-ages-of-man-1515.jpg",
        "question": "balance_elements",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_the-agony-in-the-garden.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_the-blinding-of-elymas-cartoon-for-the-sistine-chapel.jpg",
        "question": "balance_elements",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-mantegna_samson-and-delilah-1506.jpg",
        "question": "eye_movement_2",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_st-peter-enthroned-with-saints.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "andrea-del-sarto_stories-of-joseph-1.jpg",
        "question": "eye_movement_2",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_four-saints-from-left-st-peter-st-martha-st-mary-magdalene-st-leonard-1517.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "lorenzo-lotto_christ-s-farewell-to-mary-1521.jpg",
        "question": "foreground_background_4",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "giorgione_musical-instruments-music-1510(1).jpg",
        "question": "foreground_background_4",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_the-adoration-of-the-magi-1518(2).jpg",
        "question": "focus_point",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "pietro-perugino_the-vision-of-st-bernard.jpg",
        "question": "focus_point",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "raphael_st-cecilia-with-saints-detail-1516-1.jpg",
        "question": "focus_point",
        "model": "cogvlm",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "correggio_adoration-of-the-christ-child(2).jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_presentation-of-the-virgin-at-the-temple.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "deepseek",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    },
    {
        "image_filename": "cima-da-conegliano_st-peter-enthroned-with-saints.jpg",
        "question": "symmetry_asymmetry_1",
        "model": "llava",
        "contestant_1": "",
        "contestant_2": "",
        "data_type": "renaissance"
    }
];