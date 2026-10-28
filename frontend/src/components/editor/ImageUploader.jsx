import { useEffect, useRef, useState } from 'react';
import { AlertCircle, ImagePlus, Star, Trash2, UploadCloud } from 'lucide-react';
import { api } from '../../api/client';

const ALLOWED_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/avif'];
const MAX_SIZE = 5 * 1024 * 1024;

const createUid = () => `img-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;

export const ImageUploader = ({ recipeId, value, onChange, pendingProgress = {}, error }) => {
  const { uploaded = [], pending = [], coverKey = null } = value || {};

  const [progress, setProgress] = useState({});
  const [busy, setBusy] = useState(false);
  const [localError, setLocalError] = useState(null);
  const [dragActive, setDragActive] = useState(false);
  const inputRef = useRef(null);
  const pendingRef = useRef(pending);

  useEffect(() => {
    pendingRef.current = pending;
  }, [pending]);

  useEffect(
    () => () => {
      pendingRef.current.forEach((item) => URL.revokeObjectURL(item.previewUrl));
    },
    [],
  );

  const displayedError = error || localError;

  const acceptFiles = async (fileList) => {
    const files = Array.from(fileList || []);
    if (files.length === 0) return;

    setLocalError(null);

    const valid = [];
    for (const file of files) {
      if (!ALLOWED_TYPES.includes(file.type)) {
        setLocalError('Chỉ hỗ trợ ảnh định dạng JPG, PNG, WEBP hoặc AVIF.');
        continue;
      }
      if (file.size > MAX_SIZE) {
        setLocalError('Mỗi ảnh chỉ được tối đa 5MB.');
        continue;
      }
      valid.push(file);
    }

    if (valid.length === 0) return;

    if (!recipeId) {
      const queued = valid.map((file) => ({
        uid: createUid(),
        file,
        fileName: file.name,
        previewUrl: URL.createObjectURL(file),
      }));

      const nextPending = [...pending, ...queued];
      const nextCover = coverKey || (nextPending.length > 0 ? `pending:${nextPending[0].uid}` : null);
      onChange({ uploaded, pending: nextPending, coverKey: nextCover });
      return;
    }

    setBusy(true);
    const uploadedNext = [...uploaded];
    let nextCover = coverKey;

    for (const file of valid) {
      const uid = createUid();
      setProgress((prev) => ({ ...prev, [uid]: 0 }));

      try {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('isPrimary', String(!nextCover));

        const image = await api.upload(`/recipes/${recipeId}/images`, formData, (percent) => {
          setProgress((prev) => ({ ...prev, [uid]: percent }));
        });

        uploadedNext.push(image);
        if (!nextCover) nextCover = image.id;
      } catch (err) {
        setLocalError(err.message || 'Tải ảnh lên thất bại.');
      } finally {
        setProgress((prev) => {
          const next = { ...prev };
          delete next[uid];
          return next;
        });
      }
    }

    setBusy(false);
    onChange({ uploaded: uploadedNext, pending, coverKey: nextCover });
  };

  const handleInputChange = async (event) => {
    const files = event.target.files;
    event.target.value = '';
    await acceptFiles(files);
  };

  const handleDrop = async (event) => {
    event.preventDefault();
    setDragActive(false);
    await acceptFiles(event.dataTransfer.files);
  };

  const handleRemovePending = (uid) => {
    const target = pending.find((item) => item.uid === uid);
    if (target) URL.revokeObjectURL(target.previewUrl);

    const nextPending = pending.filter((item) => item.uid !== uid);
    let nextCover = coverKey;
    if (coverKey === `pending:${uid}`) {
      nextCover = nextPending[0] ? `pending:${nextPending[0].uid}` : (uploaded[0]?.id || null);
    }

    onChange({ uploaded, pending: nextPending, coverKey: nextCover });
  };

  const handleRemoveUploaded = async (image) => {
    if (!window.confirm('Bạn có chắc chắn muốn xóa ảnh này khỏi công thức?')) return;

    try {
      await api.delete(`/recipes/${recipeId}/images/${image.id}`);
      const nextUploaded = uploaded.filter((item) => item.id !== image.id);
      let nextCover = coverKey;
      if (coverKey === image.id) {
        nextCover = nextUploaded[0]?.id || null;
      }
      onChange({ uploaded: nextUploaded, pending, coverKey: nextCover });
    } catch (err) {
      setLocalError(err.message || 'Không thể xóa ảnh.');
    }
  };

  const handleChooseCover = (key) => {
    onChange({ uploaded, pending, coverKey: key });
  };

  const progressFor = (uid) => {
    if (Object.prototype.hasOwnProperty.call(pendingProgress, uid)) {
      return pendingProgress[uid];
    }
    return progress[uid];
  };

  const activeProgress = pending
    .map((item) => progressFor(item.uid))
    .filter((value) => typeof value === 'number' && value < 100);

  return (
    <div>
      <div className="editor-list-actions">
        <h2 className="editor-section-title" style={{ margin: 0, border: 'none', padding: 0 }}>
          Hình Ảnh Món Ăn ({uploaded.length + pending.length})
        </h2>
        <button
          type="button"
          className="btn btn-outline btn-sm"
          onClick={() => inputRef.current?.click()}
          disabled={busy}
        >
          <ImagePlus size={14} />
          <span>{busy ? 'Đang tải lên...' : 'Chọn ảnh'}</span>
        </button>
      </div>

      <p className="editor-tip">
        Hỗ trợ JPG, PNG, WEBP, AVIF — tối đa 5MB mỗi ảnh. Ảnh đầu tiên sẽ được đặt làm bìa nếu bạn chưa chọn.
      </p>

      {displayedError && (
        <div className="alert alert-error" style={{ display: 'flex', gap: '0.5rem', alignItems: 'center' }}>
          <AlertCircle size={16} />
          <span>{displayedError}</span>
        </div>
      )}

      {activeProgress.length > 0 && (
        <div className="uploader-progress-panel">
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8125rem', marginBottom: '0.375rem' }}>
            <span>Đang tải ảnh lên máy chủ...</span>
            <strong>{Math.min(...activeProgress)}%</strong>
          </div>
          <div className="progress-track">
            <div className="progress-fill" style={{ width: `${Math.min(...activeProgress)}%` }} />
          </div>
        </div>
      )}

      <div
        className={`uploader-dropzone${dragActive ? ' drag-active' : ''}`}
        onDragOver={(event) => {
          event.preventDefault();
          setDragActive(true);
        }}
        onDragLeave={() => setDragActive(false)}
        onDrop={handleDrop}
        onClick={() => inputRef.current?.click()}
        role="button"
        tabIndex={0}
        onKeyDown={(event) => {
          if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            inputRef.current?.click();
          }
        }}
      >
        <UploadCloud size={30} style={{ color: 'var(--text-muted)', marginBottom: '0.5rem' }} />
        <p style={{ fontWeight: 600, marginBottom: '0.25rem' }}>Kéo thả ảnh vào đây hoặc bấm để chọn</p>
        <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
          {recipeId
            ? 'Ảnh được tải lên ngay sau khi chọn.'
            : 'Ảnh sẽ được tải lên sau khi tạo công thức thành công.'}
        </p>
        <input
          ref={inputRef}
          type="file"
          accept={ALLOWED_TYPES.join(',')}
          multiple
          style={{ display: 'none' }}
          onChange={handleInputChange}
        />
      </div>

      {(uploaded.length > 0 || pending.length > 0) && (
        <div className="uploader-grid" style={{ marginTop: '1.25rem' }}>
          {uploaded.map((image) => {
            const isCover = coverKey === image.id || (!coverKey && image.isPrimary);
            return (
              <div className={`uploader-tile${isCover ? ' is-cover' : ''}`} key={image.id}>
                <img src={image.thumbnailUrl || image.originalUrl} alt={image.altText || 'Ảnh công thức'} />

                {isCover && (
                  <span className="uploader-cover-badge">
                    <Star size={11} /> Ảnh bìa
                  </span>
                )}

                <div className="uploader-tile-actions">
                  {!isCover && (
                    <button
                      type="button"
                      className="icon-btn"
                      title="Đặt làm ảnh bìa"
                      aria-label="Đặt làm ảnh bìa"
                      onClick={() => handleChooseCover(image.id)}
                    >
                      <Star size={14} />
                    </button>
                  )}
                  <button
                    type="button"
                    className="icon-btn danger"
                    title="Xóa ảnh"
                    aria-label="Xóa ảnh"
                    onClick={() => handleRemoveUploaded(image)}
                  >
                    <Trash2 size={14} />
                  </button>
                </div>
              </div>
            );
          })}

          {pending.map((item) => {
            const percent = progressFor(item.uid);
            const isCover = coverKey === `pending:${item.uid}`;

            return (
              <div className={`uploader-tile pending${isCover ? ' is-cover' : ''}`} key={item.uid}>
                <img src={item.previewUrl} alt={item.fileName} />

                {isCover && (
                  <span className="uploader-cover-badge">
                    <Star size={11} /> Ảnh bìa
                  </span>
                )}

                {typeof percent === 'number' && (
                  <div className="uploader-pending-overlay">
                    <div className="progress-track">
                      <div className="progress-fill" style={{ width: `${percent}%` }} />
                    </div>
                    <span>{percent}%</span>
                  </div>
                )}

                <div className="uploader-tile-actions">
                  {!isCover && (
                    <button
                      type="button"
                      className="icon-btn"
                      title="Đặt làm ảnh bìa"
                      aria-label="Đặt làm ảnh bìa"
                      onClick={() => handleChooseCover(`pending:${item.uid}`)}
                    >
                      <Star size={14} />
                    </button>
                  )}
                  <button
                    type="button"
                    className="icon-btn danger"
                    title="Bỏ ảnh này"
                    aria-label="Bỏ ảnh này"
                    onClick={() => handleRemovePending(item.uid)}
                  >
                    <Trash2 size={14} />
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};
