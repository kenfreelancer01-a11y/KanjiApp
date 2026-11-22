# Tập viết Kanji

Web app học kanji: tập viết theo nét, luyện tập và trắc nghiệm, theo cấp độ (Lớp 1–6, Trung học), mỗi bài 10 chữ.
Chạy được trên điện thoại như một app (PWA) và hoạt động offline sau lần mở đầu tiên.

## Cách đưa lên GitHub và dùng trên điện thoại

1. Vào github.com, tạo repository mới (ví dụ `kanji-app`), để **Public**.
2. Bấm **Add file → Upload files**, kéo thả **toàn bộ nội dung** thư mục này (gồm `index.html`, `manifest.webmanifest`,
   `sw.js`, thư mục `icons`, `data`, `tools`, `README.md`, `CREDITS.md`) rồi bấm **Commit changes**.
   (Nếu kéo thả thư mục không được, hãy tải lên từng file và tạo thư mục bằng cách gõ `icons/tên-file` ở ô tên.)
3. Vào **Settings → Pages**, ở mục *Build and deployment* chọn **Deploy from a branch**, nhánh **main**, thư mục **/(root)**, bấm **Save**.
4. Đợi 1–2 phút, địa chỉ app sẽ là `https://<tên-tài-khoản>.github.io/kanji-app/`.
5. Mở địa chỉ đó trên điện thoại, rồi:
   - **Android (Chrome):** menu ⋮ → *Cài đặt ứng dụng* hoặc *Thêm vào màn hình chính*.
   - **iPhone (Safari):** nút Chia sẻ → *Thêm vào MH chính*.

## Lưu ý

- **Tiến độ học lưu trên từng điện thoại** (trong trình duyệt). Xóa dữ liệu trình duyệt hoặc gỡ app sẽ mất tiến độ,
  và không đồng bộ giữa các máy.
- **Giọng đọc tiếng Nhật** dùng giọng có sẵn trong điện thoại. Nếu máy không có giọng Nhật, app dùng tiếng chuông.
- **Font Klee One** tải từ Google Fonts ở lần mở đầu (cần mạng), sau đó được lưu lại. Nếu chưa tải được, app dùng font hệ thống.
- **Chế độ thử:** hiện Luyện tập và Trắc nghiệm đang mở khóa toàn bộ. Để bật lại quy tắc "mở khóa đủ 10 chữ trong bài",
  mở `index.html` và đổi `var DEV_ALL=true;` thành `var DEV_ALL=false;`.
- **Cập nhật app:** thay file `index.html` trên GitHub, đồng thời đổi `kanji-v1` thành `kanji-v2` (v3, ...) trong `sw.js`.
  Trên điện thoại có thể cần mở lại app hai lần để thấy bản mới.
- **Bản quyền:** dữ liệu nét viết từ KanjiVG (CC BY-SA 3.0), xem `CREDITS.md`. Repo Public sẽ công khai cả dữ liệu trong
  bảng Excel của bạn, hãy chắc chắn bạn được phép đăng.

## Cấu trúc

- `index.html`: toàn bộ app (đã gồm dữ liệu 2136 chữ).
- `data/kanji.json`: cùng bộ dữ liệu ở dạng tách riêng (dùng khi làm app Android sau này).
- `tools/make_data.py`: tạo lại `kanji.json` từ KanjiVG và bảng Excel khi bổ sung dữ liệu.
- `sw.js`, `manifest.webmanifest`, `icons/`: để cài như app và chạy offline.
