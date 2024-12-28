CREATE TABLE 使用者表 (
    使用者名稱 NVARCHAR(50) PRIMARY KEY, -- 主鍵，作為其他表的連接鍵
    電子郵件 NVARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE 興趣標籤表 (
    標籤編號 INT IDENTITY(1,1) PRIMARY KEY, -- 主鍵
    標籤名稱 NVARCHAR(50) NOT NULL,
    使用者名稱 NVARCHAR(50) NOT NULL, -- 外鍵
    FOREIGN KEY (使用者名稱) REFERENCES 使用者表(使用者名稱)
);

CREATE TABLE 學習進度表 (
    進度編號 INT IDENTITY(1,1) PRIMARY KEY, -- 主鍵
    使用者名稱 NVARCHAR(50) NOT NULL, -- 外鍵
    課程名稱 NVARCHAR(100) NOT NULL,
    完成狀態 NVARCHAR(20) DEFAULT '未開始',
    更新時間 DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (使用者名稱) REFERENCES 使用者表(使用者名稱)
);

-- 插入使用者資料
INSERT INTO 使用者表 (使用者名稱, 電子郵件)
VALUES 
('小明', 'xiaoming@example.com'),
('小華', 'xiaohua@example.com'),
('小美', 'xiaomei@example.com'),
('阿強', 'ajiang@example.com'),
('大東', 'dadong@example.com'),
('大偉', 'david@example.com'),
('阿麗', 'ali@example.com'),
('小光', 'xiaoguang@example.com'),
('阿芬', 'afen@example.com'),
('小玉', 'xiaoyu@example.com');

-- 插入興趣標籤資料
INSERT INTO 興趣標籤表 (標籤名稱, 使用者名稱)
VALUES 
('烹飪', '小明'),
('音樂', '小華'),
('健身', '小美'),
('攝影', '阿強'),
('繪畫', '大東'),
('瑜伽', '大偉'),
('釣魚', '阿麗'),
('手作', '小光'),
('品酒', '阿芬'),
('動畫', '小玉');

-- 插入學習進度資料
INSERT INTO 學習進度表 (使用者名稱, 課程名稱, 完成狀態)
VALUES 
('小明', '如何挑選烹飪器具', '已完成'),
('小華', '吉他和弦基礎', '進行中'),
('小美', '健身訓練Ch1', '未開始'),
('阿強', '攝影基礎', '未開始'),
('大東', '素描技巧', '進行中'),
('大偉', '瑜伽基礎', '已完成');

-- 查詢使用者表
SELECT * FROM 使用者表;

-- 查詢興趣標籤表
SELECT * FROM 興趣標籤表;

-- 查詢學習進度表
SELECT * FROM 學習進度表;


-- 查詢使用者與其學習進度
SELECT lp.使用者名稱, lp.課程名稱, lp.完成狀態
FROM 學習進度表 lp;

SELECT TOP 10 * FROM 使用者表; 

-- 查詢使用者名稱與興趣
SELECT 使用者名稱, 標籤名稱
FROM 興趣標籤表;

SELECT 
    使用者表.使用者名稱, 
    使用者表.電子郵件, 
    學習進度表.課程名稱, 
    學習進度表.完成狀態 
FROM 使用者表
JOIN 學習進度表 
    ON 使用者表.使用者名稱 = 學習進度表.使用者名稱;
