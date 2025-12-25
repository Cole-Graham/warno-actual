example:

```py
    # edit template members
    components = dissolvebutton.by_member("Components").v

    # Split at the last occurrence of '] +' to separate main components from concatenated part
    main_components_str, concatenated_part = components.rsplit("] +", 1)
    main_components_str = main_components_str + "]"
    concatenated_part = "+" + concatenated_part

    # Parse the main components part back into an NDF List
    main_components = ndf.convert(main_components_str)

    inner_list = main_components[0].v
    # Apply modifications to the components

    # Convert the modified components back to string using ndf printer and recombine
    from ndf_parse import printer

    modified_components_str = printer.string(main_components)
    final_components_str = modified_components_str + concatenated_part

    # Set the final value as a string
    dissolvebutton.by_member("Components").v = final_components_str
```