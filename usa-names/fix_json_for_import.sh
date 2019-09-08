sed 's/$/,/' usa_names_count_by_year_state_raw.json > usa_names_count_by_year_state.json
sed -i '1 s/^/[/' usa_names_count_by_year_state.json
sed -i '$ s/.$/]/' usa_names_count_by_year_state.json

cat <(head -n 50 usa_names.json) <(tail -n 50 usa_names.json) > usa_names_test.json