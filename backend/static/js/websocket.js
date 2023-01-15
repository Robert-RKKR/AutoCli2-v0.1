function collect_notifications(task_type) {
    var socket = new WebSocket("ws://127.0.0.1:8000/ws/notification/");

    socket.onmessage = function(event) {
        var collect = event.data;
        console.log(collect)
        document.querySelector("#collect_output").innerText = collect;
    }
}
collect_notifications()
