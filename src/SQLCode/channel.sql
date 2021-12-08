CREATE TABLE IF NOT EXISTS public."channel"
(
    id_record serial NOT NULL,
    channel_name text,
    channel_id character varying,
    view_count character varying,
    subscriber_count character varying,
    video_count character varying,
    PRIMARY KEY (id_record)
);