if [ ! -f "$MODEL_FILE" ]; then
  echo "モデルファイルをダウンロードしています..."
  curl -L "$MODEL_URL" -o "$MODEL_FILE"
else
  echo "モデルファイルはすでにあります"
fi

uvicorn main:app --host 0.0.0.0 --port $PORT
