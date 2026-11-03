# Hướng dẫn chỉnh sửa sau này

Mặc định dự án giữ nguyên tất cả giá trị và logic; dưới đây chỉ là bản đồ vị trí để tùy chỉnh trong tương lai.

## scripts/locketfix8.js
- `mapping`, `NMS`, `locketGold`: phản hồi RevenueCat và thông tin đăng ký.
- `is_sandbox`, `expires_date`, `product_identifier`: các trường dữ liệu của phản hồi (không chứng minh đăng ký thật).

## scripts/header7.js
- `setHeaderValue` và `X-RevenueCat-ETag`: HTTP header.

## scripts/forceGold4.3.js
- `feature_gates`, `upsell_features`: cờ tính năng/paywall.
- `history_ads_*`, `sentry_*`: quảng cáo và theo dõi lỗi.
- `camera`, `camera_roll`, `camera_filter_config`: camera, video, bộ lọc.
- `max_friends_count`, `friends_sheet_locket_count_config`: bạn bè.
- `moment_views_*`, `streak_config`, `chat_reactions_enabled`: lịch sử và tin nhắn.
- `widget_*`, `journal_settings`: widget và giao diện.
- `cdn_*`, `image_cache_*`, `storage_*`: lưu trữ và cache.
- `overlay_dynamic_captions`, `overlay_items`: toàn bộ caption, emoji, màu sắc.

## Cách giữ an toàn
1. Sao lưu file trước khi chỉnh sửa (thư mục `backup/` đã có bản gốc).
2. Mỗi lần chỉ thay đổi một nhóm giá trị.
3. Kiểm tra cú pháp JavaScript: `node --check scripts/ten-file.js`.
4. Đừng tự nhận một tính năng hoạt động chỉ vì cờ đã bật. Có thể máy chủ xác thực và bác bỏ.
5. Không chia sẻ công khai dữ liệu cá nhân hoặc thông tin đăng nhập trong repo.
