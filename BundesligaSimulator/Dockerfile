# 1) Build: Blazor WASM publishen
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish -c Release -o /out --nologo

# 2) Runtime: statische Files via Nginx ausliefern
FROM nginx:alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /out/wwwroot /usr/share/nginx/html
EXPOSE 80
CMD ["nginx","-g","daemon off;"]
