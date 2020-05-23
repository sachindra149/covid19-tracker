const appUrl = window.location.href;
let returnValue = {};

async function displayHome() {
    await fetch(appUrl + "getTotalCases")
        .then((response) => response.json())
        .then((data) => {
            returnValue = data;
        });
    return returnValue;
}
$(document).ready(function () {
    console.log(appUrl);
    if (appUrl.indexOf("countries") > 0) {
        $("#example").DataTable();
    }
    displayHome().then(() => {
        console.log(returnValue);
    });
    if (appUrl.indexOf("faqs") > 0) {
        $(".faqs a").on("click", function (e) {
            e.preventDefault();
            let displayedId = $(this).attr("id").replace("question", "answer");
            $(".faqs div").css({ height: "0px", display: "none" });
            $("#" + displayedId).css({ height: "auto", display: "block" });
        });
    }
});
