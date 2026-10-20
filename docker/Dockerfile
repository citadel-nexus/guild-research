# File: docker/Dockerfile
# Stage: 11_COMMIT
# SRS: SRS-CN-RESEARCH-BUILD-001
# CAPS: pending
# CK: pending
# Dispatch: DISP-BUILD-research
# Seat: BITS-CODEGEN
# Owner: Citadel Nexus Inc.
# Created: 2026-10-20
# Depends: package.json, .nvmrc
# EnumType: ConfigDoc
# EnumEdges: DEPENDS_ON package.json; DEPENDS_ON .nvmrc
# DAG Node: none
# Intent: Align container compilation and runtime with the pinned Node release.

FROM node:24.13.0-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:24.13.0-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
EXPOSE 8200
CMD ["node", "dist/index.js"]
