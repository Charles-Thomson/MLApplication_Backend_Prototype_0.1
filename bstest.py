def dict_test():
    """test doc"""
    holder_a: dict = {"nest_a": {"egg_a": 1, "egg_b": 2}}
    holder_b: dict = {"nest_b": {"egg_c": 3, "egg_d": 4}}

    main_holder = {}
    val_a = "a"
    val_b = "b"
    main_holder[f"holder_{val_a}"] = holder_a
    main_holder[f"holder_{val_b}"] = holder_b

    print(main_holder)


dict_test()
