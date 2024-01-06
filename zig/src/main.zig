const std = @import("std");
const zap = @import("zap");

fn on_request_verbose(r: zap.SimpleRequest) void {

    r.sendBody("<html><body>This is a web page.</body></html>") catch return;
}

fn on_request_minimal(r: zap.SimpleRequest) void {
    r.sendBody("<html><body>This is a web page.</body></html>") catch return;
}

pub fn main() !void {
    var listener = zap.SimpleHttpListener.init(.{
        .port = 8080,
        .on_request = on_request_verbose,
        .log = true,
        .max_clients = 100000,
    });
    try listener.listen();

    std.debug.print("Listening on 0.0.0.0:8080\n", .{});

    // start worker threads
    zap.start(.{
        .threads = 4,
        .workers = 4,
    });
}