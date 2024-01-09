use hyper::{Body, Response, Server};
use hyper::service::{make_service_fn, service_fn};
use std::convert::Infallible;

async fn handle_request(_req: hyper::Request<Body>) -> Result<Response<Body>, Infallible> {
    Ok(Response::new(Body::from("<html><body>This is a web page.</body></html>")))
}

#[tokio::main]
async fn main() {
    let addr = ([0, 0, 0, 0], 8080).into();
    let service = make_service_fn(|_| async { Ok::<_, Infallible>(service_fn(handle_request)) });

    let server = Server::bind(&addr).serve(service);

    if let Err(e) = server.await {
        eprintln!("server error: {}", e);
    }
}
