FROM alpine:latest

LABEL maintainer="yash <yashwanths1111@gmail.com>"

# Install nginx, curl, and netstat (via net-tools)
RUN apk --no-cache add nginx curl net-tools && \
    adduser -D -g 'nginx' nginx && \
    mkdir -p /run/nginx

# Copy default.conf (should be customized) and app content
COPY default.conf /etc/nginx/http.d/default.conf
COPY 2048/ /usr/share/nginx/html/

# Set correct ownership
RUN chown -R nginx:nginx /usr/share/nginx/html

# Expose HTTP port
EXPOSE 80

# Run container as non-root for security
USER nginx

# Start NGINX in foreground
CMD ["nginx", "-g", "daemon off;"]
# ENTRYPOINT ["nginx", "-g", "daemon off;"]
