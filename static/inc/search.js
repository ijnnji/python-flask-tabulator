const input = document.getElementById("fSearch");
input.addEventListener("keyup", function() {
    table.setFilter(matchAny, { value: input.value });
    if (input.value == " ") {
        table.clearFilter()
    }
});
function matchAny(data, filterParams) {
      //data - the data for the row being filtered
      //filterParams - params object passed to the filter
      //RegExp - modifier "i" - case insensitve

    var match = false;
    const regex = RegExp(filterParams.value, 'i');

    for (var key in data) {
        if (regex.test(data[key]) == true) {
            match = true;
        }
    }
    return match;
}

