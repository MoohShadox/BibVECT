area = document.getElementById('review');
render = document.getElementById('render');

render_button = document.getElementById("render-button")
view_p = document.getElementById("reviewP")
if(view_p)
{
    var md = window.markdownit();
    var rez = md.render(view_p.innerHTML);
    console.log("CLICK")
    view_p.innerHTML = rez;
    MathJax.typeset();
}

$("#render-button").on("click", function () {
    var md = window.markdownit();
    var rez = md.render(area.value);
    render.innerHTML = rez;
    MathJax.typeset();
});


