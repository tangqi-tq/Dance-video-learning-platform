/*
 Navicat Premium Data Transfer

 Source Server         : business_card
 Source Server Type    : MySQL
 Source Server Version : 80039
 Source Host           : localhost:3306
 Source Schema         : business_card

 Target Server Type    : MySQL
 Target Server Version : 80039
 File Encoding         : 65001

 Date: 14/06/2026 10:52:15
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for assignments
-- ----------------------------
DROP TABLE IF EXISTS `assignments`;
CREATE TABLE `assignments`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NULL DEFAULT NULL COMMENT '学员ID',
  `video_id` int NULL DEFAULT NULL COMMENT '关联视频ID',
  `video_url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '作业视频',
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '作业说明',
  `submit_time` datetime NULL DEFAULT NULL COMMENT '提交时间',
  `score` int NULL DEFAULT NULL COMMENT '评分',
  `teacher_comment` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '老师点评',
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT '待批改' COMMENT '状态',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 25 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of assignments (已脱敏真实姓名)
-- ----------------------------
INSERT INTO `assignments` VALUES (1, 1, 1, 'assignments_videos/1_student_01_20260601_201647.mp4', '热身动作练习，请老师点评', '2026-06-01 20:16:48', 9, '动作标准，节奏感不错！继续保持', '已批改');
INSERT INTO `assignments` VALUES (2, 1, 2, 'assignments_videos/1_student_01_20260605_151230.mp4', '律动练习作业', '2026-06-05 15:12:30', 8, '律动感很好，注意身体协调性', '已批改');
INSERT INTO `assignments` VALUES (3, 2, 12, 'assignments_videos/2_student_02_20260602_091500.mp4', '伦巴基本步练习', '2026-06-02 09:15:00', 9, '步伐准确，胯部动作还需要加强', '已批改');
INSERT INTO `assignments` VALUES (4, 2, 13, 'assignments_videos/2_student_02_20260606_140000.mp4', '恰恰步练习', '2026-06-06 14:00:00', 8, '节奏感好，注意手部动作', '已批改');
INSERT INTO `assignments` VALUES (5, 3, 20, 'assignments_videos/3_student_03_20260603_103000.mp4', '芭蕾手位练习', '2026-06-03 10:30:00', 10, '非常标准！体态优美', '已批改');
INSERT INTO `assignments` VALUES (6, 3, 21, 'assignments_videos/3_student_03_20260607_160000.mp4', '脚位组合练习', '2026-06-07 16:00:00', 9, '脚位准确，注意转开', '已批改');
INSERT INTO `assignments` VALUES (7, 4, 27, 'assignments_videos/4_student_04_20260604_113000.mp4', '身韵基础练习', '2026-06-04 11:30:00', 8, '身韵不错，呼吸配合需要加强', '已批改');
INSERT INTO `assignments` VALUES (8, 5, 37, 'assignments_videos/5_student_05_20260605_193000.mp4', '爵士律动练习', '2026-06-05 19:30:00', 8, '律动感很好，继续努力', '已批改');
INSERT INTO `assignments` VALUES (9, 6, 5, 'assignments_videos/6_student_06_20260601_143000.mp4', 'Popping元素练习', '2026-06-01 14:30:00', 9, 'Pop很清晰，力度控制不错', '已批改');
INSERT INTO `assignments` VALUES (10, 6, 6, 'assignments_videos/6_student_06_20260606_163000.mp4', 'Locking动作练习', '2026-06-06 16:30:00', 9, '动作干净利落，很不错', '已批改');
INSERT INTO `assignments` VALUES (11, 7, 15, 'assignments_videos/7_student_07_20260602_150000.mp4', '伦巴组合练习', '2026-06-02 15:00:00', 8, '组合流畅，情感表达可以更丰富', '已批改');
INSERT INTO `assignments` VALUES (12, 8, 22, 'assignments_videos/8_student_08_20260603_093000.mp4', '体态训练作业', '2026-06-03 09:30:00', 7, '体态有进步，加强核心力量', '已批改');
INSERT INTO `assignments` VALUES (13, 9, 32, 'assignments_videos/9_student_09_20260604_173000.mp4', '放松技巧练习', '2026-06-04 17:30:00', 9, '放松很到位，身体控制好', '已批改');
INSERT INTO `assignments` VALUES (14, 10, 30, 'assignments_videos/10_student_10_20260605_100000.mp4', '技巧组合练习', '2026-06-05 10:00:00', 9, '技巧掌握很好，继续加油', '已批改');
INSERT INTO `assignments` VALUES (15, 11, 38, 'assignments_videos/11_student_11_20260606_203000.mp4', 'Isolation练习', '2026-06-06 20:30:00', 7, '分离度有进步，需要更多练习', '已批改');
INSERT INTO `assignments` VALUES (16, 12, 4, 'assignments_videos/12_student_12_20260607_143000.mp4', '定点训练作业', '2026-06-07 14:30:00', 8, '定点清晰，速度可以再快些', '已批改');
INSERT INTO `assignments` VALUES (17, 13, 16, 'assignments_videos/13_student_13_20260601_163000.mp4', '恰恰高级组合', '2026-06-01 16:30:00', 9, '组合完成度高，表现力强', '已批改');
INSERT INTO `assignments` VALUES (18, 14, 24, 'assignments_videos/14_student_14_20260602_113000.mp4', '跳跃训练作业', '2026-06-02 11:30:00', 8, '跳跃高度不错，落地要更稳', '已批改');
INSERT INTO `assignments` VALUES (19, 15, 40, 'assignments_videos/15_student_15_20260603_203000.mp4', 'Power Jazz练习', '2026-06-03 20:30:00', NULL, NULL, '待批改');
INSERT INTO `assignments` VALUES (20, 16, 35, 'assignments_videos/16_student_16_20260604_183000.mp4', '编舞技巧作业', '2026-06-04 18:30:00', NULL, NULL, '待批改');
INSERT INTO `assignments` VALUES (21, 17, 11, 'assignments_videos/17_student_17_20260605_153000.mp4', '完整作品排练', '2026-06-05 15:30:00', NULL, NULL, '待批改');
INSERT INTO `assignments` VALUES (22, 18, 29, 'assignments_videos/18_student_18_20260606_113000.mp4', '傣族舞元素练习', '2026-06-06 11:30:00', NULL, NULL, '待批改');
INSERT INTO `assignments` VALUES (23, 19, 18, 'assignments_videos/19_student_19_20260607_143000.mp4', '竞技套路练习', '2026-06-07 14:30:00', NULL, NULL, '待批改');
INSERT INTO `assignments` VALUES (24, 20, 41, 'assignments_videos/20_student_20_20260601_113000.mp4', '爵士技巧练习', '2026-06-01 11:30:00', 9, '技巧掌握很好，表现力强', '已批改');
INSERT INTO `assignments` VALUES (25, 1, 1213, 'assignments_videos/1_student_01_20260613_205307.mp4', '用于小组作业', '2026-06-13 20:53:08', 10, '非常不错，显示成功', '已批改');

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS `comments`;
CREATE TABLE `comments`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NULL DEFAULT NULL COMMENT '学员ID',
  `video_id` int NULL DEFAULT NULL COMMENT '视频ID',
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '评论内容',
  `comment_time` datetime NULL DEFAULT NULL COMMENT '评论时间',
  `type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT 'student' COMMENT '类型',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comments
-- ----------------------------
INSERT INTO `comments` VALUES (1, 1, 1, '这个热身教学太实用了！', '2026-06-01 11:00:00', 'student');
INSERT INTO `comments` VALUES (2, 2, 12, '伦巴真的好美，慢慢练习中', '2026-06-02 09:30:00', 'student');
INSERT INTO `comments` VALUES (3, 3, 20, '芭蕾好优雅，喜欢', '2026-06-03 10:45:00', 'student');
INSERT INTO `comments` VALUES (4, 4, 27, '中国舞的身韵真的太有韵味了', '2026-06-04 12:00:00', 'student');
INSERT INTO `comments` VALUES (5, 5, 37, '爵士好有活力，爱了爱了', '2026-06-05 20:00:00', 'student');
INSERT INTO `comments` VALUES (6, 1, 2, '律动练习有点难，要多练', '2026-06-05 15:30:00', 'student');
INSERT INTO `comments` VALUES (7, 6, 5, 'Popping好酷！老师讲得很清楚', '2026-06-01 15:00:00', 'student');
INSERT INTO `comments` VALUES (8, 7, 15, '伦巴组合很流畅，继续努力', '2026-06-02 16:00:00', 'student');
INSERT INTO `comments` VALUES (9, 8, 22, '体态真的需要坚持练习', '2026-06-03 10:00:00', 'student');
INSERT INTO `comments` VALUES (10, 9, 32, '现代舞的感觉好自由', '2026-06-04 18:00:00', 'student');
INSERT INTO `comments` VALUES (11, 10, 30, '技巧组合很有挑战性', '2026-06-05 11:00:00', 'student');
INSERT INTO `comments` VALUES (12, 11, 38, 'Isolation练了好久才有感觉', '2026-06-06 21:00:00', 'student');
INSERT INTO `comments` VALUES (13, 12, 4, '定点训练很考验控制力', '2026-06-07 15:00:00', 'student');
INSERT INTO `comments` VALUES (14, 13, 16, '恰恰节奏好快，要跟上', '2026-06-01 17:00:00', 'student');
INSERT INTO `comments` VALUES (15, 14, 24, '跳跃好难，落地总是不稳', '2026-06-02 12:00:00', 'student');
INSERT INTO `comments` VALUES (16, 15, 40, 'Power Jazz太帅了！', '2026-06-03 21:00:00', 'student');

-- ----------------------------
-- Table structure for courses
-- ----------------------------
DROP TABLE IF EXISTS `courses`;
CREATE TABLE `courses`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '课程名称',
  `dance_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '舞种',
  `level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '难度等级',
  `cover` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '封面图片',
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL COMMENT '课程简介',
  `price` decimal(10, 2) NULL DEFAULT NULL COMMENT '价格',
  `teacher` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '授课老师',
  `create_date` date NULL DEFAULT NULL COMMENT '创建日期',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of courses
-- ----------------------------
INSERT INTO `courses` VALUES (1, '街舞入门基础', '街舞', '初级', NULL, '街舞基础动作教学，适合零基础学员。内容包括：律动、波浪、定点等基础元素。', 299.00, '王老师', '2026-01-01');
INSERT INTO `courses` VALUES (2, '街舞中级进阶', '街舞', '中级', NULL, '街舞进阶课程，学习更复杂的动作组合和风格。包含：Popping基础、Locking元素等。', 399.00, '王老师', '2026-01-10');
INSERT INTO `courses` VALUES (3, '街舞高级编舞', '街舞', '高级', NULL, '街舞高级编舞课程，学习完整舞蹈作品的编排和表演技巧。', 499.00, '王老师', '2026-01-20');
INSERT INTO `courses` VALUES (4, '拉丁舞入门', '拉丁舞', '初级', NULL, '拉丁舞基础教学，学习伦巴、恰恰的基本步伐和节奏。', 299.00, '李老师', '2026-02-01');
INSERT INTO `courses` VALUES (5, '拉丁舞中级提升', '拉丁舞', '中级', NULL, '拉丁舞进阶课程，学习更复杂的舞步组合和表现力提升。', 399.00, '李老师', '2026-02-10');
INSERT INTO `courses` VALUES (6, '拉丁舞高级竞技', '拉丁舞', '高级', NULL, '拉丁舞竞技课程，学习比赛套路和技巧，提升舞台表现力。', 499.00, '李老师', '2026-02-20');
INSERT INTO `courses` VALUES (7, '芭蕾舞基础', '芭蕾舞', '初级', NULL, '芭蕾舞基础教学，学习基本手位、脚位和体态训练。', 399.00, '张老师', '2026-03-01');
INSERT INTO `courses` VALUES (8, '芭蕾舞中级提升', '芭蕾舞', '中级', NULL, '芭蕾舞进阶课程，学习转圈、跳跃等技巧。', 499.00, '张老师', '2026-03-10');
INSERT INTO `courses` VALUES (9, '芭蕾舞高级表演', '芭蕾舞', '高级', NULL, '芭蕾舞高级课程，学习经典舞剧片段和表演技巧。', 599.00, '张老师', '2026-03-20');
INSERT INTO `courses` VALUES (10, '中国舞入门', '中国舞', '初级', NULL, '中国舞基础教学，学习基本身韵和民族民间舞元素。', 299.00, '刘老师', '2026-04-01');
INSERT INTO `courses` VALUES (11, '中国舞中级提升', '中国舞', '中级', NULL, '中国舞进阶课程，学习更复杂的身法组合和舞蹈表现。', 399.00, '刘老师', '2026-04-10');
INSERT INTO `courses` VALUES (12, '现代舞基础', '现代舞', '初级', NULL, '现代舞基础教学，学习放松技巧、地面动作和即兴元素。', 299.00, '陈老师', '2026-05-01');
INSERT INTO `courses` VALUES (13, '现代舞中级编创', '现代舞', '中级', NULL, '现代舞进阶课程，学习编舞技巧和情感表达。', 399.00, '陈老师', '2026-05-10');
INSERT INTO `courses` VALUES (14, '爵士舞入门', '爵士舞', '初级', NULL, '爵士舞基础教学，学习基本律动、Isolation和简单舞蹈片段。', 299.00, '赵老师', '2026-06-01');
INSERT INTO `courses` VALUES (15, '爵士舞中级提升', '爵士舞', '中级', NULL, '爵士舞进阶课程，学习Power Jazz和性感爵士等风格。', 399.00, '赵老师', '2026-06-10');

-- ----------------------------
-- Table structure for favorites
-- ----------------------------
DROP TABLE IF EXISTS `favorites`;
CREATE TABLE `favorites`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NULL DEFAULT NULL COMMENT '学员ID',
  `video_id` int NULL DEFAULT NULL COMMENT '视频ID',
  `add_time` datetime NULL DEFAULT NULL COMMENT '收藏时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of favorites
-- ----------------------------
INSERT INTO `favorites` VALUES (1, 1, 1, '2026-06-01 10:30:00');
INSERT INTO `favorites` VALUES (2, 1, 5, '2026-06-02 14:00:00');
INSERT INTO `favorites` VALUES (3, 2, 12, '2026-06-01 09:00:00');
INSERT INTO `favorites` VALUES (4, 2, 15, '2026-06-02 10:30:00');
INSERT INTO `favorites` VALUES (5, 3, 20, '2026-06-01 08:30:00');
INSERT INTO `favorites` VALUES (6, 3, 25, '2026-06-03 09:00:00');
INSERT INTO `favorites` VALUES (7, 4, 27, '2026-06-01 13:30:00');
INSERT INTO `favorites` VALUES (8, 5, 37, '2026-06-01 18:30:00');
INSERT INTO `favorites` VALUES (9, 6, 1, '2026-05-20 10:00:00');
INSERT INTO `favorites` VALUES (10, 6, 9, '2026-05-21 11:00:00');
INSERT INTO `favorites` VALUES (11, 7, 12, '2026-05-15 09:00:00');
INSERT INTO `favorites` VALUES (12, 7, 16, '2026-05-16 10:00:00');
INSERT INTO `favorites` VALUES (13, 8, 20, '2026-05-10 08:30:00');
INSERT INTO `favorites` VALUES (14, 9, 32, '2026-05-25 17:30:00');
INSERT INTO `favorites` VALUES (15, 10, 27, '2026-05-01 10:30:00');
INSERT INTO `favorites` VALUES (16, 10, 30, '2026-05-02 11:00:00');
INSERT INTO `favorites` VALUES (17, 11, 37, '2026-06-07 19:30:00');
INSERT INTO `favorites` VALUES (18, 12, 4, '2026-06-07 15:30:00');
INSERT INTO `favorites` VALUES (19, 13, 16, '2026-06-06 14:30:00');
INSERT INTO `favorites` VALUES (20, 14, 22, '2026-06-05 10:30:00');
INSERT INTO `favorites` VALUES (21, 15, 39, '2026-06-07 20:30:00');
INSERT INTO `favorites` VALUES (22, 16, 34, '2026-06-06 18:00:00');
INSERT INTO `favorites` VALUES (23, 17, 10, '2026-06-05 11:30:00');
INSERT INTO `favorites` VALUES (24, 18, 28, '2026-06-07 14:30:00');
INSERT INTO `favorites` VALUES (25, 19, 17, '2026-06-04 16:30:00');
INSERT INTO `favorites` VALUES (26, 20, 26, '2026-06-03 10:30:00');

-- ----------------------------
-- Table structure for learning_record
-- ----------------------------
DROP TABLE IF EXISTS `learning_record`;
CREATE TABLE `learning_record`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NULL DEFAULT NULL COMMENT '学员ID',
  `video_id` int NULL DEFAULT NULL COMMENT '视频ID',
  `watched_seconds` int NULL DEFAULT 0 COMMENT '已观看时长',
  `is_completed` tinyint NULL DEFAULT 0 COMMENT '是否完成',
  `last_watch_time` datetime NULL DEFAULT NULL COMMENT '上次观看时间',
  `watch_count` int NULL DEFAULT 1 COMMENT '观看次数',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 47 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of learning_record
-- ----------------------------
INSERT INTO `learning_record` VALUES (1, 1, 1, 300, 1, '2026-06-01 10:30:00', 3);
INSERT INTO `learning_record` VALUES (2, 1, 2, 450, 1, '2026-06-02 14:20:00', 2);
INSERT INTO `learning_record` VALUES (3, 1, 3, 380, 1, '2026-06-03 09:15:00', 1);
INSERT INTO `learning_record` VALUES (4, 1, 4, 420, 1, '2026-06-04 16:45:00', 2);
INSERT INTO `learning_record` VALUES (5, 1, 5, 500, 1, '2026-06-05 11:00:00', 1);
INSERT INTO `learning_record` VALUES (6, 1, 6, 480, 0, '2026-06-06 15:30:00', 1);
INSERT INTO `learning_record` VALUES (7, 2, 12, 350, 1, '2026-06-01 09:00:00', 2);
INSERT INTO `learning_record` VALUES (8, 2, 13, 380, 1, '2026-06-02 10:30:00', 2);
INSERT INTO `learning_record` VALUES (9, 2, 14, 300, 1, '2026-06-03 14:00:00', 1);
INSERT INTO `learning_record` VALUES (10, 2, 15, 500, 1, '2026-06-04 16:20:00', 1);
INSERT INTO `learning_record` VALUES (11, 2, 16, 520, 0, '2026-06-05 19:00:00', 1);
INSERT INTO `learning_record` VALUES (12, 3, 20, 400, 1, '2026-06-01 08:30:00', 3);
INSERT INTO `learning_record` VALUES (13, 3, 21, 350, 1, '2026-06-02 09:00:00', 2);
INSERT INTO `learning_record` VALUES (14, 3, 22, 420, 1, '2026-06-03 10:15:00', 2);
INSERT INTO `learning_record` VALUES (15, 3, 23, 500, 1, '2026-06-04 14:30:00', 2);
INSERT INTO `learning_record` VALUES (16, 3, 24, 480, 1, '2026-06-05 15:45:00', 1);
INSERT INTO `learning_record` VALUES (17, 3, 25, 600, 0, '2026-06-06 19:00:00', 1);
INSERT INTO `learning_record` VALUES (18, 4, 27, 400, 1, '2026-06-01 13:00:00', 2);
INSERT INTO `learning_record` VALUES (19, 4, 28, 450, 1, '2026-06-02 14:30:00', 1);
INSERT INTO `learning_record` VALUES (20, 4, 29, 430, 1, '2026-06-03 16:00:00', 2);
INSERT INTO `learning_record` VALUES (21, 5, 37, 350, 1, '2026-06-01 18:30:00', 3);
INSERT INTO `learning_record` VALUES (22, 5, 38, 380, 1, '2026-06-02 19:00:00', 2);
INSERT INTO `learning_record` VALUES (23, 5, 39, 450, 0, '2026-06-03 20:30:00', 1);
INSERT INTO `learning_record` VALUES (24, 6, 1, 300, 1, '2026-05-20 10:00:00', 4);
INSERT INTO `learning_record` VALUES (25, 6, 2, 450, 1, '2026-05-21 11:00:00', 3);
INSERT INTO `learning_record` VALUES (26, 6, 5, 500, 1, '2026-05-22 14:00:00', 2);
INSERT INTO `learning_record` VALUES (27, 6, 6, 480, 1, '2026-05-23 15:00:00', 2);
INSERT INTO `learning_record` VALUES (28, 6, 9, 520, 1, '2026-05-24 16:00:00', 1);
INSERT INTO `learning_record` VALUES (29, 7, 12, 350, 1, '2026-05-15 09:00:00', 3);
INSERT INTO `learning_record` VALUES (30, 7, 15, 500, 1, '2026-05-16 10:30:00', 2);
INSERT INTO `learning_record` VALUES (31, 8, 20, 400, 1, '2026-05-10 08:00:00', 3);
INSERT INTO `learning_record` VALUES (32, 8, 21, 350, 1, '2026-05-11 09:00:00', 2);
INSERT INTO `learning_record` VALUES (33, 9, 32, 380, 1, '2026-05-25 17:00:00', 2);
INSERT INTO `learning_record` VALUES (34, 9, 33, 420, 1, '2026-05-26 18:00:00', 1);
INSERT INTO `learning_record` VALUES (35, 10, 27, 400, 1, '2026-05-01 10:00:00', 3);
INSERT INTO `learning_record` VALUES (36, 10, 30, 550, 1, '2026-05-02 14:00:00', 2);
INSERT INTO `learning_record` VALUES (37, 11, 37, 350, 1, '2026-06-07 19:00:00', 2);
INSERT INTO `learning_record` VALUES (38, 12, 4, 420, 1, '2026-06-07 16:00:00', 1);
INSERT INTO `learning_record` VALUES (39, 13, 16, 520, 1, '2026-06-06 15:00:00', 2);
INSERT INTO `learning_record` VALUES (40, 14, 22, 420, 1, '2026-06-05 10:00:00', 1);
INSERT INTO `learning_record` VALUES (41, 15, 39, 450, 1, '2026-06-07 20:00:00', 1);
INSERT INTO `learning_record` VALUES (42, 16, 34, 450, 1, '2026-06-06 17:30:00', 2);
INSERT INTO `learning_record` VALUES (43, 17, 10, 480, 1, '2026-06-05 11:00:00', 1);
INSERT INTO `learning_record` VALUES (44, 18, 28, 450, 0, '2026-06-07 14:00:00', 1);
INSERT INTO `learning_record` VALUES (45, 19, 17, 450, 1, '2026-06-04 16:00:00', 2);
INSERT INTO `learning_record` VALUES (46, 20, 26, 520, 1, '2026-06-03 10:00:00', 1);
INSERT INTO `learning_record` VALUES (47, 1, 23, 500, 1, '2026-06-13 20:49:49', 2);
INSERT INTO `learning_record` VALUES (48, 1, 24, 480, 1, '2026-06-13 20:50:31', 1);
INSERT INTO `learning_record` VALUES (49, 4, 1, 300, 1, '2026-06-13 20:51:24', 1);

-- ----------------------------
-- Table structure for students
-- ----------------------------
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '姓名',
  `nickname` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '昵称',
  `mobile` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '手机号',
  `wechat` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '微信号',
  `dance_level` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '舞龄等级',
  `dance_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '擅长舞种',
  `register_date` date NULL DEFAULT NULL COMMENT '注册日期',
  `avatar` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '头像路径',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of students (已全面脱敏：姓名替换为学员XX，手机号替换为假号码，微信号替换为假ID)
-- ----------------------------
INSERT INTO `students` VALUES (1, '学员01', '小01', '13800000001', 'wx_01', '中级', '街舞', '2026-01-15', NULL);
INSERT INTO `students` VALUES (2, '学员02', '小02', '13800000002', 'wx_02', '初级', '拉丁舞', '2026-01-20', NULL);
INSERT INTO `students` VALUES (3, '学员03', '小03', '13800000003', 'wx_03', '高级', '芭蕾舞', '2026-02-10', NULL);
INSERT INTO `students` VALUES (4, '学员04', '小04', '13800000004', 'wx_04', '中级', '中国舞', '2026-02-15', NULL);
INSERT INTO `students` VALUES (5, '学员05', '小05', '13800000005', 'wx_05', '初级', '爵士舞', '2026-03-01', NULL);
INSERT INTO `students` VALUES (6, '学员06', '小06', '13800000006', 'wx_06', '高级', '街舞', '2026-03-10', NULL);
INSERT INTO `students` VALUES (7, '学员07', '小07', '13800000007', 'wx_07', '中级', '拉丁舞', '2026-03-15', NULL);
INSERT INTO `students` VALUES (8, '学员08', '小08', '13800000008', 'wx_08', '初级', '芭蕾舞', '2026-04-01', NULL);
INSERT INTO `students` VALUES (9, '学员09', '小09', '13800000009', 'wx_09', '中级', '现代舞', '2026-04-10', NULL);
INSERT INTO `students` VALUES (10, '学员10', '小10', '13800000010', 'wx_10', '高级', '中国舞', '2026-04-15', NULL);
INSERT INTO `students` VALUES (11, '学员11', '小11', '13800000011', 'wx_11', '初级', '爵士舞', '2026-05-01', NULL);
INSERT INTO `students` VALUES (12, '学员12', '小12', '13800000012', 'wx_12', '中级', '街舞', '2026-05-05', NULL);
INSERT INTO `students` VALUES (13, '学员13', '小13', '13800000013', 'wx_13', '高级', '拉丁舞', '2026-05-10', NULL);
INSERT INTO `students` VALUES (14, '学员14', '小14', '13800000014', 'wx_14', '初级', '芭蕾舞', '2026-05-15', NULL);
INSERT INTO `students` VALUES (15, '学员15', '小15', '13800000015', 'wx_15', '中级', '爵士舞', '2026-05-20', NULL);
INSERT INTO `students` VALUES (16, '学员16', '小16', '13800000016', 'wx_16', '中级', '现代舞', '2026-06-01', NULL);
INSERT INTO `students` VALUES (17, '学员17', '小17', '13800000017', 'wx_17', '高级', '街舞', '2026-06-02', NULL);
INSERT INTO `students` VALUES (18, '学员18', '小18', '13800000018', 'wx_18', '初级', '中国舞', '2026-06-03', NULL);
INSERT INTO `students` VALUES (20, '学员20', '小20', '13800000020', 'wx_20', '高级', '芭蕾舞', '2026-06-05', NULL);
INSERT INTO `students` VALUES (21, '学员21', '小21', '13800000021', 'wx_21', '高级', '爵士舞', '2026-06-13', NULL);
INSERT INTO `students` VALUES (22, '学员22', '小22', '13800000022', 'wx_22', '初级', '街舞', '2026-06-13', NULL);

-- ----------------------------
-- Table structure for videos
-- ----------------------------
DROP TABLE IF EXISTS `videos`;
CREATE TABLE `videos`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_id` int NULL DEFAULT NULL COMMENT '所属课程ID',
  `title` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '视频标题',
  `url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '视频链接',
  `duration` int NULL DEFAULT NULL COMMENT '视频时长（秒）',
  `sort_order` int NULL DEFAULT NULL COMMENT '排序',
  `thumbnail` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '缩略图',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 43 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of videos
-- ----------------------------
INSERT INTO `videos` VALUES (1, 1, '街舞热身运动', 'https://www.w3schools.com/html/mov_bbb.mp4', 300, 1, NULL);
INSERT INTO `videos` VALUES (2, 1, '街舞基础律动', 'https://www.w3schools.com/html/mov_bbb.mp4', 450, 2, NULL);
INSERT INTO `videos` VALUES (3, 1, '街舞波浪动作', 'https://www.w3schools.com/html/mov_bbb.mp4', 380, 3, NULL);
INSERT INTO `videos` VALUES (4, 1, '街舞定点训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 420, 4, NULL);
INSERT INTO `videos` VALUES (5, 2, 'Popping基础元素', 'https://www.w3schools.com/html/mov_bbb.mp4', 500, 1, NULL);
INSERT INTO `videos` VALUES (6, 2, 'Locking基本动作', 'https://www.w3schools.com/html/mov_bbb.mp4', 480, 2, NULL);
INSERT INTO `videos` VALUES (7, 2, 'Breaking地板动作', 'https://www.w3schools.com/html/mov_bbb.mp4', 600, 3, NULL);
INSERT INTO `videos` VALUES (8, 2, '街舞风格融合', 'https://www.w3schools.com/html/mov_bbb.mp4', 550, 4, NULL);
INSERT INTO `videos` VALUES (9, 3, '街舞编舞技巧', 'https://www.w3schools.com/html/mov_bbb.mp4', 520, 1, NULL);
INSERT INTO `videos` VALUES (10, 3, '舞台表演训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 480, 2, NULL);
INSERT INTO `videos` VALUES (11, 3, '完整作品排练', 'https://www.w3schools.com/html/mov_bbb.mp4', 720, 3, NULL);
INSERT INTO `videos` VALUES (12, 4, '伦巴基本步', 'https://www.w3schools.com/html/mov_bbb.mp4', 350, 1, NULL);
INSERT INTO `videos` VALUES (13, 4, '恰恰基本步', 'https://www.w3schools.com/html/mov_bbb.mp4', 380, 2, NULL);
INSERT INTO `videos` VALUES (14, 4, '拉丁舞节奏训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 300, 3, NULL);
INSERT INTO `videos` VALUES (15, 5, '伦巴组合套路', 'https://www.w3schools.com/html/mov_bbb.mp4', 500, 1, NULL);
INSERT INTO `videos` VALUES (16, 5, '恰恰高级组合', 'https://www.w3schools.com/html/mov_bbb.mp4', 520, 2, NULL);
INSERT INTO `videos` VALUES (17, 5, '拉丁舞表现力', 'https://www.w3schools.com/html/mov_bbb.mp4', 450, 3, NULL);
INSERT INTO `videos` VALUES (18, 6, '竞技套路编排', 'https://www.w3schools.com/html/mov_bbb.mp4', 600, 1, NULL);
INSERT INTO `videos` VALUES (19, 6, '比赛技巧训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 550, 2, NULL);
INSERT INTO `videos` VALUES (20, 7, '芭蕾手位训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 400, 1, NULL);
INSERT INTO `videos` VALUES (21, 7, '芭蕾脚位训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 350, 2, NULL);
INSERT INTO `videos` VALUES (22, 7, '芭蕾体态训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 420, 3, NULL);
INSERT INTO `videos` VALUES (23, 8, '芭蕾转圈技巧', 'https://www.w3schools.com/html/mov_bbb.mp4', 500, 1, NULL);
INSERT INTO `videos` VALUES (24, 8, '芭蕾跳跃训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 480, 2, NULL);
INSERT INTO `videos` VALUES (25, 9, '天鹅湖片段', 'https://www.w3schools.com/html/mov_bbb.mp4', 600, 1, NULL);
INSERT INTO `videos` VALUES (26, 9, '芭蕾表演技巧', 'https://www.w3schools.com/html/mov_bbb.mp4', 520, 2, NULL);
INSERT INTO `videos` VALUES (27, 10, '中国舞身韵基础', 'https://www.w3schools.com/html/mov_bbb.mp4', 400, 1, NULL);
INSERT INTO `videos` VALUES (28, 10, '藏族舞元素', 'https://www.w3schools.com/html/mov_bbb.mp4', 450, 2, NULL);
INSERT INTO `videos` VALUES (29, 10, '傣族舞元素', 'https://www.w3schools.com/html/mov_bbb.mp4', 430, 3, NULL);
INSERT INTO `videos` VALUES (30, 11, '中国舞技巧组合', 'https://www.w3schools.com/html/mov_bbb.mp4', 550, 1, NULL);
INSERT INTO `videos` VALUES (31, 11, '古典舞身法', 'https://www.w3schools.com/html/mov_bbb.mp4', 500, 2, NULL);
INSERT INTO `videos` VALUES (32, 12, '现代舞放松技巧', 'https://www.w3schools.com/html/mov_bbb.mp4', 380, 1, NULL);
INSERT INTO `videos` VALUES (33, 12, '地面动作训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 420, 2, NULL);
INSERT INTO `videos` VALUES (34, 12, '现代舞即兴', 'https://www.w3schools.com/html/mov_bbb.mp4', 450, 3, NULL);
INSERT INTO `videos` VALUES (35, 13, '现代舞编舞技巧', 'https://www.w3schools.com/html/mov_bbb.mp4', 520, 1, NULL);
INSERT INTO `videos` VALUES (36, 13, '情感表达训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 480, 2, NULL);
INSERT INTO `videos` VALUES (37, 14, '爵士舞律动', 'https://www.w3schools.com/html/mov_bbb.mp4', 350, 1, NULL);
INSERT INTO `videos` VALUES (38, 14, '爵士舞Isolation', 'https://www.w3schools.com/html/mov_bbb.mp4', 380, 2, NULL);
INSERT INTO `videos` VALUES (39, 14, '爵士舞基础舞蹈', 'https://www.w3schools.com/html/mov_bbb.mp4', 450, 3, NULL);
INSERT INTO `videos` VALUES (40, 15, 'Power Jazz训练', 'https://www.w3schools.com/html/mov_bbb.mp4', 500, 1, NULL);
INSERT INTO `videos` VALUES (41, 15, '性感爵士技巧', 'https://www.w3schools.com/html/mov_bbb.mp4', 480, 2, NULL);
INSERT INTO `videos` VALUES (42, 15, '爵士舞综合编排', 'https://www.w3schools.com/html/mov_bbb.mp4', 550, 3, NULL);

SET FOREIGN_KEY_CHECKS = 1;