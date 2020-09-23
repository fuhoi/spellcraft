const fs = require("fs");
const Papa = require("papaparse");


function csv2json(file) {

  try {
    const file_path = `../src/assets/data/${file}`;
    console.log('file_path=', file_path);

    if (!fs.existsSync(file_path)) {
      throw new Error('File does not exist.');
    }

    const csv_data = fs.readFileSync(file_path, { encoding: "utf-8" });
    console.log('csv_data=', csv_data);

    const json_data = Papa.parse(csv_data, {
      delimiter: ",",
      newline: "\r\n",
      quoteChar: "\"",
      escapeChar: "\"",
      header: true,
      dynamicTyping: true,
      encoding: "utf-8",
      skipEmptyLines: true,
    });
    console.log("json_data:", json_data);

    let array_data = json_data.data;
    // NOTE: If fields include code and name and code is blank, replace with snake case name
    if (json_data.meta.fields.includes("code") && json_data.meta.fields.includes("name")) {
      array_data = array_data.map(row => {
        if (row) {
          const codeIsEmpty = (row.code || '').length === 0;
          const nameIsEmpty = (row.name || '').length === 0;
          if (codeIsEmpty && !nameIsEmpty) {
            row.code = row.name.toLowerCase().replace(/\W/g, '_').replace(/_+/g, '_');
          }
        }
        return row;
      });
    }
    console.log("array_data:", array_data);

    const string_data = JSON.stringify(array_data, null, 2) + "\r\n";
    fs.writeFileSync(`${file_path}.json`, string_data, { encoding: "utf-8" });

  } catch (err) {

    console.error('err=', err);

  }

}


csv2json("elements.csv");
csv2json("modes.csv");
csv2json("categories.csv");
csv2json("spells.csv");
