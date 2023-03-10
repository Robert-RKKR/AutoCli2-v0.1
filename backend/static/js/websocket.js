function addMessage(collected_object) {
    const newDiv = document.createElement("div");
    const newContent = document.createTextNode(collected_object.message);
    newDiv.appendChild(newContent);
    const currentDiv = document.getElementById("collect_output");
    currentDiv.appendChild(newDiv);
}


function collect_notifications(task_type) {
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/notification/");

    socket.onmessage = function(event) {
        var collect = event.data;
        var collect_json = JSON.parse(collect)
        addMessage(collect_json)
    }
}
collect_notifications()
