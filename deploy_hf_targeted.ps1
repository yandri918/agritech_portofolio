# ============================================================
# Targeted Deploy: AgriSensa Utama -> Hugging Face Space
# Clone HF Space, copy only relevant app files, push back
# ============================================================

param(
    [string]$HfToken = ""
)

$HF_REPO = "https://huggingface.co/spaces/yandri918/agrisensa_utama"
$CLONE_DIR = "$env:TEMP\hf_agrisensa_deploy"
$SRC = "C:\Users\yandr\OneDrive\Desktop\agrisensa-api"

Write-Host "🚀 AgriSensa -> Hugging Face Targeted Deploy" -ForegroundColor Cyan
Write-Host ""

# Step 1: Clone the HF Space (shallow)
if (Test-Path $CLONE_DIR) {
    Write-Host "🗑️  Removing old clone dir..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force $CLONE_DIR
}

Write-Host "📥 Cloning HF Space (shallow)..." -ForegroundColor Yellow
git clone --depth=1 $HF_REPO $CLONE_DIR
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Clone failed. Ensure you're logged in to HF: huggingface-cli login" -ForegroundColor Red
    exit 1
}

Write-Host "✅ Clone success!" -ForegroundColor Green
Write-Host ""

# Step 2: Copy app files
Write-Host "📂 Copying app files..." -ForegroundColor Yellow

$DIRS_TO_COPY = @(
    "agrisensa_streamlit",
    "agrisensa_biz",
    "agrisensa_tech",
    "agrisensa_commodities",
    "agrisensa_livestock",
    "agrisensa_eco",
    "ekonometrika_pro",
    "app",
    ".streamlit"
)

$FILES_TO_COPY = @(
    "requirements.txt",
    "Procfile"
)

foreach ($dir in $DIRS_TO_COPY) {
    $srcPath = Join-Path $SRC $dir
    $dstPath = Join-Path $CLONE_DIR $dir
    if (Test-Path $srcPath) {
        Write-Host "  ↳ Copying $dir ..." -ForegroundColor Gray
        if (Test-Path $dstPath) { Remove-Item -Recurse -Force $dstPath }
        Copy-Item -Recurse -Force $srcPath $dstPath
    } else {
        Write-Host "  ⚠️  Skipping $dir (not found)" -ForegroundColor DarkYellow
    }
}

foreach ($file in $FILES_TO_COPY) {
    $srcPath = Join-Path $SRC $file
    if (Test-Path $srcPath) {
        Write-Host "  ↳ Copying $file ..." -ForegroundColor Gray
        Copy-Item -Force $srcPath $CLONE_DIR
    }
}

# Step 3: Copy ML models (only small ones)
Write-Host "  ↳ Copying ML models (small)..." -ForegroundColor Gray
$MODELS = @(
    "advanced_yield_model.pkl",
    "crop_recommendation_model.pkl",
    "bwd_model.pkl",
    "recommendation_model.pkl",
    "success_model.pkl",
    "shap_explainer.pkl"
)
foreach ($model in $MODELS) {
    $srcPath = Join-Path $SRC $model
    if (Test-Path $srcPath) {
        Copy-Item -Force $srcPath $CLONE_DIR
    }
}

# Step 4: Write correct README.md for HF
Write-Host ""
Write-Host "📝 Writing HF-compatible README.md..." -ForegroundColor Yellow

$hfReadme = @"
---
title: AgriSensa Intelligence
emoji: 🛰️
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: 1.32.0
app_file: agrisensa_streamlit/Home.py
pinned: false
---

# 🛰️ AgriSensa Intelligence Ecosystem v5.0

Advanced agricultural super-app powered by Machine Learning, Explainable AI (SHAP), and real-time market intelligence.

Built for Indonesian precision farming. Includes RAB calculator, crop yield prediction, market intelligence, and more.
"@

Set-Content -Path (Join-Path $CLONE_DIR "README.md") -Value $hfReadme
Write-Host "✅ README.md written!" -ForegroundColor Green

# Step 5: Commit & Push
Write-Host ""
Write-Host "🚀 Committing and pushing to HF Space..." -ForegroundColor Yellow

Set-Location $CLONE_DIR
git config user.email "deploy@agrisensa.ai"
git config user.name "AgriSensa Deploy Bot"
git add .
git commit -m "deploy: AgriSensa Intelligence Ecosystem v5.0"
git push origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "✅ Deployment successful!" -ForegroundColor Green
    Write-Host "🌐 Space URL: https://huggingface.co/spaces/yandri918/agrisensa_utama" -ForegroundColor Cyan
    Write-Host "⏳ Space will rebuild in ~2-3 minutes." -ForegroundColor Yellow
} else {
    Write-Host "❌ Push failed. Check if you are logged in: huggingface-cli login" -ForegroundColor Red
}

Set-Location $SRC
