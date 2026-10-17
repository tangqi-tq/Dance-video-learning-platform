# PyQt5 模块
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# 内置模块
import sys
import os
import shutil
from datetime import datetime
from config import DB_CONFIG
# 第三方模块
import pandas as pd
from sqlalchemy import create_engine, text



# 颜色主题配置
COLORS = {
    'bg_main': '#1a1a2e',
    'bg_panel': '#16213e',
    'primary': '#ff6b6b',
    'primary_dark': '#ee5a5a',
    'primary_light': '#ff8e8e',
    'text_light': '#eeeeee',
    'text_muted': '#aaaaaa',
    'border': '#0f3460',
    'success': '#4ecdc4',
    'warning': '#ffe66d',
    'table_header': '#0f3460',
    'tab_bg': '#1a1a2e',
}

# ==================== 全局样式表  ====================
GLOBAL_STYLE = f"""
QMainWindow {{
    background-color: {COLORS['bg_main']};
}}

QWidget {{
    background-color: {COLORS['bg_main']};
}}

QTabWidget::pane {{
    border: 2px solid {COLORS['border']};
    background-color: {COLORS['bg_panel']};
    border-radius: 10px;
    margin-top: -2px;
}}

QTabBar::tab {{
    background-color: #2d2d44;
    color: {COLORS['text_muted']};
    padding: 12px 35px;
    font-size: 15px;
    font-weight: bold;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    margin-right: 5px;
    min-width: 100px;
}}

QTabBar::tab:hover {{
    background-color: {COLORS['primary_dark']};
    color: white;
}}

QTabBar::tab:selected {{
    background-color: {COLORS['primary']};
    color: white;
}}

QPushButton {{
    background-color: {COLORS['primary']};
    color: white;
    border: none;
    padding: 8px 18px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: bold;
    min-height: 20px;
}}

QPushButton:hover {{
    background-color: {COLORS['primary_dark']};
}}

QPushButton:pressed {{
    background-color: {COLORS['primary_light']};
}}

QTableWidget {{
    background-color: {COLORS['bg_panel']};
    alternate-background-color: #1e2a4a;
    gridline-color: {COLORS['border']};
    color: {COLORS['text_light']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    selection-background-color: {COLORS['primary']};
}}

QTableWidget::item {{
    padding: 8px;
}}

QTableWidget::item:selected {{
    background-color: {COLORS['primary']};
    color: white;
}}

QHeaderView::section {{
    background-color: {COLORS['table_header']};
    color: {COLORS['text_light']};
    padding: 10px;
    border: none;
    font-weight: bold;
    font-size: 13px;
}}

QLabel {{
    color: {COLORS['text_light']};
    font-size: 13px;
    background: transparent;
}}

/* ========== 下拉框样式修复 - 字体颜色改为白色 ========== */
QComboBox {{
    background-color: #0f1a2e;
    color: {COLORS['text_light']};  /* 字体颜色：亮白色 */
    border: 1px solid {COLORS['border']};
    border-radius: 6px;
    padding: 8px;
    font-size: 13px;
    min-width: 150px;
}}

QComboBox:hover {{
    border: 1px solid {COLORS['primary']};
}}

QComboBox:focus {{
    border: 2px solid {COLORS['primary']};
}}

QComboBox::drop-down {{
    border: none;
    width: 20px;
}}

QComboBox::down-arrow {{
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 5px solid {COLORS['primary']};
    margin-right: 5px;
}}

/* 下拉列表选项样式 */
QComboBox QAbstractItemView {{
    background-color: #0f1a2e;
    color: {COLORS['text_light']};  /* 下拉选项字体颜色：亮白色 */
    selection-background-color: {COLORS['primary']};
    selection-color: white;
    border: 1px solid {COLORS['border']};
    outline: none;
}}

QComboBox QAbstractItemView::item {{
    padding: 8px;
    min-height: 25px;
}}

QComboBox QAbstractItemView::item:hover {{
    background-color: {COLORS['primary_dark']};
    color: white;
}}

/* 普通输入框样式 */
QLineEdit, QTextEdit {{
    background-color: #0f1a2e;
    color: {COLORS['text_light']};
    border: 1px solid {COLORS['border']};
    border-radius: 6px;
    padding: 8px;
    font-size: 13px;
}}

QLineEdit:focus, QTextEdit:focus {{
    border: 2px solid {COLORS['primary']};
}}

QDialog {{
    background-color: {COLORS['bg_panel']};
}}

QDialog QLabel {{
    color: {COLORS['text_light']};
}}

QMessageBox {{
    background-color: {COLORS['bg_panel']};
}}

QMessageBox QLabel {{
    color: {COLORS['text_light']};
    min-width: 300px;
}}

QSlider::groove:horizontal {{
    border: 1px solid {COLORS['border']};
    height: 6px;
    background: {COLORS['bg_main']};
    border-radius: 3px;
}}

QSlider::handle:horizontal {{
    background: {COLORS['primary']};
    border: none;
    width: 16px;
    height: 16px;
    margin: -6px 0;
    border-radius: 8px;
}}

QSlider::handle:horizontal:hover {{
    background: {COLORS['primary_dark']};
    width: 18px;
    height: 18px;
}}

QScrollBar:vertical {{
    background: {COLORS['bg_main']};
    width: 12px;
    border-radius: 6px;
}}

QScrollBar::handle:vertical {{
    background: {COLORS['primary']};
    border-radius: 6px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background: {COLORS['primary_dark']};
}}

QScrollBar:horizontal {{
    background: {COLORS['bg_main']};
    height: 12px;
    border-radius: 6px;
}}

QScrollBar::handle:horizontal {{
    background: {COLORS['primary']};
    border-radius: 6px;
    min-width: 30px;
}}

QScrollBar::handle:horizontal:hover {{
    background: {COLORS['primary_dark']};
}}

QStatusBar {{
    background-color: {COLORS['bg_panel']};
    color: {COLORS['text_muted']};
    border-top: 1px solid {COLORS['border']};
    padding: 5px;
}}

QGroupBox {{
    color: {COLORS['primary']};
    border: 1px solid {COLORS['border']};
    border-radius: 8px;
    margin-top: 10px;
    padding-top: 10px;
    font-weight: bold;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
}}
"""


def get_engine():
    return create_engine(
        f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}?charset={DB_CONFIG['charset']}")


# ==================== 主窗口 ====================
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("舞蹈视频教学平台")
        self.setGeometry(100, 100, 1300, 800)

        self.setStyleSheet(GLOBAL_STYLE)
        self.setWindowIcon(QIcon())

        self.video_save_dir = os.path.join(os.getcwd(), "assignments_videos")
        if not os.path.exists(self.video_save_dir):
            os.makedirs(self.video_save_dir)

        self.setup_ui()
        self.show_students()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        # 顶部标题栏
        title_widget = QWidget()
        title_widget.setObjectName("TitleWidget")
        title_widget.setStyleSheet(f"""
            #TitleWidget {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {COLORS['primary']}, stop:0.5 #ff7e5e, stop:1 {COLORS['primary_dark']});
                border-radius: 15px;
            }}
        """)
        title_widget.setFixedHeight(80)
        title_layout = QHBoxLayout(title_widget)
        title_layout.setContentsMargins(25, 10, 25, 10)

        logo_label = QLabel("💃")
        logo_label.setStyleSheet("font-size: 40px; background: transparent;")
        title_layout.addWidget(logo_label)

        title_label = QLabel("舞蹈视频教学平台")
        title_label.setStyleSheet(
            "font-size: 28px; font-weight: bold; color: white; background: transparent; font-family: 'Microsoft YaHei';")
        title_label.setAlignment(Qt.AlignCenter)
        title_layout.addWidget(title_label, 1)

        subtitle_label = QLabel("Dance Teaching Platform")
        subtitle_label.setStyleSheet(
            "font-size: 14px; color: rgba(255,255,255,0.85); background: transparent; font-style: italic;")
        title_layout.addWidget(subtitle_label)

        main_layout.addWidget(title_widget)

        # 标签页
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.North)
        self.tab_widget.setTabShape(QTabWidget.Rounded)

        self.students_tab = QWidget()
        self.courses_tab = QWidget()
        self.videos_tab = QWidget()
        self.learning_tab = QWidget()
        self.assignments_tab = QWidget()

        for tab in [self.students_tab, self.courses_tab, self.videos_tab, self.learning_tab, self.assignments_tab]:
            tab.setAttribute(Qt.WA_StyledBackground, True)
            tab.setStyleSheet("QWidget { background-color: transparent; }")

        self.tab_widget.addTab(self.students_tab, "  📋 学员管理  ")
        self.tab_widget.addTab(self.courses_tab, "  📚 课程管理  ")
        self.tab_widget.addTab(self.videos_tab, "  🎬 视频管理  ")
        self.tab_widget.addTab(self.learning_tab, "  📊 学习记录  ")
        self.tab_widget.addTab(self.assignments_tab, "  📝 作业管理  ")

        main_layout.addWidget(self.tab_widget)

        self.statusBar().showMessage("✅ 系统就绪 | 欢迎使用舞蹈教学平台")

        self.tab_widget.currentChanged.connect(self.on_tab_changed)

    def on_tab_changed(self, index):
        tab_names = ["学员管理", "课程管理", "视频管理", "学习记录", "作业管理"]
        if index < len(tab_names):
            self.statusBar().showMessage(f"📌 当前页面：{tab_names[index]} | 数据已刷新")

        if index == 0:
            self.show_students()
        elif index == 1:
            self.show_courses()
        elif index == 2:
            self.show_videos()
        elif index == 3:
            self.show_learning_records()
        elif index == 4:
            self.show_assignments()

    def clear_layout(self, widget):
        if widget.layout():
            old_layout = widget.layout()
            while old_layout.count():
                item = old_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
            QWidget().setLayout(old_layout)

    # ==================== 学员管理 ====================
    def show_students(self):
        self.clear_layout(self.students_tab)

        layout = QVBoxLayout(self.students_tab)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        toolbar = QHBoxLayout()
        btn_add = QPushButton("➕ 添加学员")
        btn_add.setCursor(Qt.PointingHandCursor)
        btn_add.clicked.connect(self.add_student)
        btn_refresh = QPushButton("🔄 刷新")
        btn_refresh.setCursor(Qt.PointingHandCursor)
        btn_refresh.clicked.connect(lambda: self.show_students())
        toolbar.addWidget(btn_add)
        toolbar.addWidget(btn_refresh)
        toolbar.addStretch()

        try:
            engine = get_engine()
            with engine.connect() as conn:
                result = conn.execute(text("SELECT COUNT(*) as cnt FROM students"))
                count = result.fetchone()[0]
                stats_label = QLabel(f"📊 学员总数：{count} 人")
                stats_label.setStyleSheet(
                    f"color: {COLORS['primary']}; font-weight: bold; font-size: 14px; background: transparent; padding: 5px 10px;")
                toolbar.addWidget(stats_label)
        except:
            pass

        layout.addLayout(toolbar)

        self.students_table = QTableWidget()
        self.students_table.setAlternatingRowColors(True)
        self.students_table.setColumnCount(7)
        self.students_table.setHorizontalHeaderLabels(
            ["ID", "姓名", "昵称", "手机号", "微信号", "舞龄等级", "擅长舞种"])
        self.students_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.students_table.setEditTriggers(QTableWidget.NoEditTriggers)

        try:
            engine = get_engine()
            df = pd.read_sql("SELECT * FROM students ORDER BY id", engine)

            self.students_table.setRowCount(len(df))
            for i in range(len(df)):
                row = df.iloc[i]
                self.students_table.setItem(i, 0, QTableWidgetItem(str(row['id']) if pd.notna(row['id']) else ""))
                self.students_table.setItem(i, 1, QTableWidgetItem(str(row['name']) if pd.notna(row['name']) else ""))
                self.students_table.setItem(i, 2,
                                            QTableWidgetItem(str(row['nickname']) if pd.notna(row['nickname']) else ""))
                self.students_table.setItem(i, 3,
                                            QTableWidgetItem(str(row['mobile']) if pd.notna(row['mobile']) else ""))
                self.students_table.setItem(i, 4,
                                            QTableWidgetItem(str(row['wechat']) if pd.notna(row['wechat']) else ""))
                self.students_table.setItem(i, 5, QTableWidgetItem(
                    str(row['dance_level']) if pd.notna(row['dance_level']) else ""))
                self.students_table.setItem(i, 6, QTableWidgetItem(
                    str(row['dance_type']) if pd.notna(row['dance_type']) else ""))

            self.students_table.resizeColumnsToContents()
        except Exception as e:
            print(f"加载学员数据出错: {e}")

        layout.addWidget(self.students_table)

        btn_layout = QHBoxLayout()
        btn_edit = QPushButton("✏️ 编辑")
        btn_edit.setCursor(Qt.PointingHandCursor)
        btn_edit.clicked.connect(self.edit_student)
        btn_delete = QPushButton("🗑️ 删除")
        btn_delete.setCursor(Qt.PointingHandCursor)
        btn_delete.clicked.connect(self.delete_student)
        btn_layout.addWidget(btn_edit)
        btn_layout.addWidget(btn_delete)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

    def add_student(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("添加学员")
        dialog.setModal(True)
        dialog.resize(420, 320)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        name_input = QLineEdit()
        name_input.setPlaceholderText("请输入姓名")
        nickname_input = QLineEdit()
        nickname_input.setPlaceholderText("请输入昵称")
        mobile_input = QLineEdit()
        mobile_input.setPlaceholderText("请输入手机号")
        wechat_input = QLineEdit()
        wechat_input.setPlaceholderText("请输入微信号")
        level_combo = QComboBox()
        level_combo.addItems(["初级", "中级", "高级"])
        dance_combo = QComboBox()
        dance_combo.addItems(["街舞", "拉丁舞", "芭蕾舞", "中国舞", "现代舞", "爵士舞"])

        layout.addRow("姓名 *:", name_input)
        layout.addRow("昵称:", nickname_input)
        layout.addRow("手机号:", mobile_input)
        layout.addRow("微信号:", wechat_input)
        layout.addRow("舞龄等级:", level_combo)
        layout.addRow("擅长舞种:", dance_combo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted:
            if name_input.text().strip():
                try:
                    engine = get_engine()
                    df = pd.DataFrame([{
                        'name': name_input.text(),
                        'nickname': nickname_input.text(),
                        'mobile': mobile_input.text(),
                        'wechat': wechat_input.text(),
                        'dance_level': level_combo.currentText(),
                        'dance_type': dance_combo.currentText(),
                        'register_date': datetime.now().date()
                    }])
                    df.to_sql('students', engine, if_exists='append', index=False)
                    QMessageBox.information(self, "成功", "学员添加成功！")
                    self.show_students()
                except Exception as e:
                    QMessageBox.warning(self, "错误", f"添加失败：{e}")
            else:
                QMessageBox.warning(self, "提示", "姓名不能为空！")

    def edit_student(self):
        current_row = self.students_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "提示", "请先选择要编辑的学员")
            return

        student_id = self.students_table.item(current_row, 0).text()
        old_name = self.students_table.item(current_row, 1).text()
        old_nickname = self.students_table.item(current_row, 2).text()
        old_mobile = self.students_table.item(current_row, 3).text()
        old_wechat = self.students_table.item(current_row, 4).text()
        old_level = self.students_table.item(current_row, 5).text()
        old_dance_type = self.students_table.item(current_row, 6).text()

        dialog = QDialog(self)
        dialog.setWindowTitle(f"编辑学员 - {old_name}")
        dialog.setModal(True)
        dialog.resize(420, 320)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        name_input = QLineEdit(old_name)
        nickname_input = QLineEdit(old_nickname if old_nickname != "" else "")
        mobile_input = QLineEdit(old_mobile if old_mobile != "" else "")
        wechat_input = QLineEdit(old_wechat if old_wechat != "" else "")

        level_combo = QComboBox()
        level_combo.addItems(["初级", "中级", "高级"])
        level_index = level_combo.findText(old_level)
        if level_index >= 0:
            level_combo.setCurrentIndex(level_index)

        dance_combo = QComboBox()
        dance_combo.addItems(["街舞", "拉丁舞", "芭蕾舞", "中国舞", "现代舞", "爵士舞"])
        dance_index = dance_combo.findText(old_dance_type)
        if dance_index >= 0:
            dance_combo.setCurrentIndex(dance_index)

        layout.addRow("姓名 *:", name_input)
        layout.addRow("昵称:", nickname_input)
        layout.addRow("手机号:", mobile_input)
        layout.addRow("微信号:", wechat_input)
        layout.addRow("舞龄等级:", level_combo)
        layout.addRow("擅长舞种:", dance_combo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted:
            if name_input.text().strip():
                try:
                    engine = get_engine()
                    with engine.connect() as conn:
                        conn.execute(text(f"""
                            UPDATE students 
                            SET name = '{name_input.text()}',
                                nickname = '{nickname_input.text()}',
                                mobile = '{mobile_input.text()}',
                                wechat = '{wechat_input.text()}',
                                dance_level = '{level_combo.currentText()}',
                                dance_type = '{dance_combo.currentText()}'
                            WHERE id = {student_id}
                        """))
                        conn.commit()
                    QMessageBox.information(self, "成功", "学员信息修改成功！")
                    self.show_students()
                except Exception as e:
                    QMessageBox.warning(self, "错误", f"修改失败：{e}")
            else:
                QMessageBox.warning(self, "提示", "姓名不能为空！")

    def delete_student(self):
        current_row = self.students_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "提示", "请先选择要删除的学员")
            return

        student_id = self.students_table.item(current_row, 0).text()
        student_name = self.students_table.item(current_row, 1).text()
        reply = QMessageBox.question(self, "确认", f"确定要删除学员【{student_name}】吗？",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                engine = get_engine()
                with engine.connect() as conn:
                    conn.execute(text(f"DELETE FROM students WHERE id = {student_id}"))
                    conn.commit()
                QMessageBox.information(self, "成功", "删除成功！")
                self.show_students()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"删除失败：{e}")

    # ==================== 课程管理 ====================
    def show_courses(self):
        self.clear_layout(self.courses_tab)

        layout = QVBoxLayout(self.courses_tab)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        toolbar = QHBoxLayout()
        btn_add = QPushButton("➕ 添加课程")
        btn_add.setCursor(Qt.PointingHandCursor)
        btn_add.clicked.connect(self.add_course)
        btn_refresh = QPushButton("🔄 刷新")
        btn_refresh.setCursor(Qt.PointingHandCursor)
        btn_refresh.clicked.connect(lambda: self.show_courses())
        toolbar.addWidget(btn_add)
        toolbar.addWidget(btn_refresh)
        toolbar.addStretch()
        layout.addLayout(toolbar)

        self.courses_table = QTableWidget()
        self.courses_table.setAlternatingRowColors(True)
        self.courses_table.setColumnCount(7)
        self.courses_table.setHorizontalHeaderLabels(["ID", "课程名称", "舞种", "难度", "价格", "老师", "创建日期"])
        self.courses_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.courses_table.setEditTriggers(QTableWidget.NoEditTriggers)

        try:
            engine = get_engine()
            df = pd.read_sql("SELECT * FROM courses ORDER BY id", engine)

            self.courses_table.setRowCount(len(df))
            for i in range(len(df)):
                row = df.iloc[i]
                self.courses_table.setItem(i, 0, QTableWidgetItem(str(row['id']) if pd.notna(row['id']) else ""))
                self.courses_table.setItem(i, 1, QTableWidgetItem(str(row['name']) if pd.notna(row['name']) else ""))
                self.courses_table.setItem(i, 2, QTableWidgetItem(
                    str(row['dance_type']) if pd.notna(row['dance_type']) else ""))
                self.courses_table.setItem(i, 3, QTableWidgetItem(str(row['level']) if pd.notna(row['level']) else ""))
                price_val = row['price'] if pd.notna(row['price']) else ""
                self.courses_table.setItem(i, 4, QTableWidgetItem(f"¥{price_val}" if price_val else ""))
                self.courses_table.setItem(i, 5,
                                           QTableWidgetItem(str(row['teacher']) if pd.notna(row['teacher']) else ""))
                self.courses_table.setItem(i, 6, QTableWidgetItem(
                    str(row['create_date']) if pd.notna(row['create_date']) else ""))

            self.courses_table.resizeColumnsToContents()
        except Exception as e:
            print(f"加载课程数据出错: {e}")

        layout.addWidget(self.courses_table)

        btn_layout = QHBoxLayout()
        btn_edit = QPushButton("✏️ 编辑")
        btn_edit.setCursor(Qt.PointingHandCursor)
        btn_edit.clicked.connect(self.edit_course)
        btn_delete = QPushButton("🗑️ 删除")
        btn_delete.setCursor(Qt.PointingHandCursor)
        btn_delete.clicked.connect(self.delete_course)
        btn_layout.addWidget(btn_edit)
        btn_layout.addWidget(btn_delete)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

    def add_course(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("添加课程")
        dialog.resize(480, 420)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        name_input = QLineEdit()
        name_input.setPlaceholderText("请输入课程名称")
        dance_combo = QComboBox()
        dance_combo.addItems(["街舞", "拉丁舞", "芭蕾舞", "中国舞", "现代舞", "爵士舞"])
        level_combo = QComboBox()
        level_combo.addItems(["初级", "中级", "高级"])
        price_input = QLineEdit()
        price_input.setPlaceholderText("请输入价格")
        teacher_input = QLineEdit()
        teacher_input.setPlaceholderText("请输入老师姓名")
        desc_input = QTextEdit()
        desc_input.setMaximumHeight(100)
        desc_input.setPlaceholderText("请输入课程简介...")

        layout.addRow("课程名称 *:", name_input)
        layout.addRow("舞种:", dance_combo)
        layout.addRow("难度:", level_combo)
        layout.addRow("价格(元):", price_input)
        layout.addRow("授课老师:", teacher_input)
        layout.addRow("课程简介:", desc_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted and name_input.text().strip():
            try:
                engine = get_engine()
                price = float(price_input.text()) if price_input.text() else None
                df = pd.DataFrame([{
                    'name': name_input.text(),
                    'dance_type': dance_combo.currentText(),
                    'level': level_combo.currentText(),
                    'price': price,
                    'teacher': teacher_input.text(),
                    'description': desc_input.toPlainText(),
                    'create_date': datetime.now().date()
                }])
                df.to_sql('courses', engine, if_exists='append', index=False)
                QMessageBox.information(self, "成功", "课程添加成功！")
                self.show_courses()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"添加失败：{e}")

    def edit_course(self):
        current_row = self.courses_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "提示", "请先选择要编辑的课程")
            return

        course_id = self.courses_table.item(current_row, 0).text()
        old_name = self.courses_table.item(current_row, 1).text()
        old_dance_type = self.courses_table.item(current_row, 2).text()
        old_level = self.courses_table.item(current_row, 3).text()
        old_price = self.courses_table.item(current_row, 4).text().replace("¥", "")
        old_teacher = self.courses_table.item(current_row, 5).text()

        dialog = QDialog(self)
        dialog.setWindowTitle(f"编辑课程 - {old_name}")
        dialog.setModal(True)
        dialog.resize(480, 420)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        name_input = QLineEdit(old_name)

        dance_combo = QComboBox()
        dance_combo.addItems(["街舞", "拉丁舞", "芭蕾舞", "中国舞", "现代舞", "爵士舞"])
        dance_index = dance_combo.findText(old_dance_type)
        if dance_index >= 0:
            dance_combo.setCurrentIndex(dance_index)

        level_combo = QComboBox()
        level_combo.addItems(["初级", "中级", "高级"])
        level_index = level_combo.findText(old_level)
        if level_index >= 0:
            level_combo.setCurrentIndex(level_index)

        price_input = QLineEdit(old_price)
        teacher_input = QLineEdit(old_teacher)

        layout.addRow("课程名称 *:", name_input)
        layout.addRow("舞种:", dance_combo)
        layout.addRow("难度:", level_combo)
        layout.addRow("价格(元):", price_input)
        layout.addRow("授课老师:", teacher_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted and name_input.text().strip():
            try:
                engine = get_engine()
                price = float(price_input.text()) if price_input.text() else "NULL"
                with engine.connect() as conn:
                    conn.execute(text(f"""
                        UPDATE courses 
                        SET name = '{name_input.text()}',
                            dance_type = '{dance_combo.currentText()}',
                            level = '{level_combo.currentText()}',
                            price = {price if price != "NULL" else 'NULL'},
                            teacher = '{teacher_input.text()}'
                        WHERE id = {course_id}
                    """))
                    conn.commit()
                QMessageBox.information(self, "成功", "课程修改成功！")
                self.show_courses()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"修改失败：{e}")

    def delete_course(self):
        current_row = self.courses_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "提示", "请先选择要删除的课程")
            return

        course_id = self.courses_table.item(current_row, 0).text()
        course_name = self.courses_table.item(current_row, 1).text()
        reply = QMessageBox.question(self, "确认", f"确定要删除课程【{course_name}】吗？\n关联的视频也会被删除。",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                engine = get_engine()
                with engine.connect() as conn:
                    conn.execute(text(f"DELETE FROM videos WHERE course_id = {course_id}"))
                    conn.execute(text(f"DELETE FROM courses WHERE id = {course_id}"))
                    conn.commit()
                QMessageBox.information(self, "成功", "删除成功！")
                self.show_courses()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"删除失败：{e}")

    # ==================== 视频管理 ====================
    def show_videos(self):
        self.clear_layout(self.videos_tab)

        layout = QVBoxLayout(self.videos_tab)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        select_layout = QHBoxLayout()
        label = QLabel("📁 选择课程:")
        label.setStyleSheet(
            f"color: {COLORS['primary']}; font-weight: bold; font-size: 14px; background: transparent;")
        select_layout.addWidget(label)

        # ========== 课程选择下拉框 - 单独设置样式确保字体白色 ==========
        self.course_combo = QComboBox()
        self.course_combo.setMinimumWidth(250)
        self.course_combo.setStyleSheet("""
            QComboBox {
                background-color: #0f1a2e;
                color: #eeeeee;
                border: 1px solid #0f3460;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #ff6b6b;
                margin-right: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #0f1a2e;
                color: #eeeeee;
                selection-background-color: #ff6b6b;
                selection-color: white;
                border: 1px solid #0f3460;
            }
            QComboBox QAbstractItemView::item {
                padding: 8px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #ee5a5a;
                color: white;
            }
        """)

        try:
            engine = get_engine()
            courses_df = pd.read_sql("SELECT id, name FROM courses", engine)
            for _, row in courses_df.iterrows():
                self.course_combo.addItem(row['name'], row['id'])
        except Exception as e:
            print(f"加载课程列表出错: {e}")

        self.course_combo.currentIndexChanged.connect(self.load_videos_by_course)
        select_layout.addWidget(self.course_combo)
        select_layout.addStretch()

        btn_add = QPushButton("➕ 添加视频")
        btn_add.setCursor(Qt.PointingHandCursor)
        btn_add.clicked.connect(self.add_video)
        btn_edit_video = QPushButton("✏️ 编辑视频")
        btn_edit_video.setCursor(Qt.PointingHandCursor)
        btn_edit_video.clicked.connect(self.edit_video)
        btn_delete_video = QPushButton("🗑️ 删除视频")
        btn_delete_video.setCursor(Qt.PointingHandCursor)
        btn_delete_video.clicked.connect(self.delete_video)
        select_layout.addWidget(btn_add)
        select_layout.addWidget(btn_edit_video)
        select_layout.addWidget(btn_delete_video)

        layout.addLayout(select_layout)

        # 视频表格 - 6列，增加记录观看按钮列
        self.videos_table = QTableWidget()
        self.videos_table.setAlternatingRowColors(True)
        self.videos_table.setColumnCount(6)
        self.videos_table.setHorizontalHeaderLabels(["ID", "视频标题", "时长(秒)", "排序", "播放", "记录观看"])
        self.videos_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.videos_table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.videos_table)

        if self.course_combo.count() > 0:
            self.load_videos_by_course()

    def load_videos_by_course(self):
        if self.course_combo.currentIndex() < 0 or self.course_combo.count() == 0:
            return

        course_id = self.course_combo.currentData()
        try:
            engine = get_engine()
            df = pd.read_sql(f"SELECT * FROM videos WHERE course_id = {course_id} ORDER BY sort_order", engine)

            self.videos_table.setRowCount(len(df))
            for i in range(len(df)):
                row = df.iloc[i]
                video_id = row['id']
                video_url = row['url'] if pd.notna(row['url']) else ""
                video_duration = row['duration'] if pd.notna(row['duration']) else 0

                self.videos_table.setItem(i, 0, QTableWidgetItem(str(video_id) if pd.notna(video_id) else ""))
                self.videos_table.setItem(i, 1, QTableWidgetItem(str(row['title']) if pd.notna(row['title']) else ""))
                self.videos_table.setItem(i, 2,
                                          QTableWidgetItem(str(video_duration) if pd.notna(video_duration) else "0"))
                self.videos_table.setItem(i, 3, QTableWidgetItem(
                    str(row['sort_order']) if pd.notna(row['sort_order']) else "0"))

                # 播放按钮
                play_btn = QPushButton("▶ 播放")
                play_btn.setCursor(Qt.PointingHandCursor)
                play_btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {COLORS['success']};
                        color: white;
                        padding: 5px 15px;
                        border-radius: 6px;
                    }}
                    QPushButton:hover {{
                        background-color: #3dbdb5;
                    }}
                """)
                play_btn.clicked.connect(lambda checked, url=video_url, vid=video_id, dur=video_duration:
                                         self.play_video(url, vid, dur))
                self.videos_table.setCellWidget(i, 4, play_btn)

                # 记录观看按钮
                record_btn = QPushButton("📝 记录观看")
                record_btn.setCursor(Qt.PointingHandCursor)
                record_btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {COLORS['warning']};
                        color: #333;
                        padding: 5px 12px;
                        border-radius: 6px;
                        font-weight: bold;
                    }}
                    QPushButton:hover {{
                        background-color: #ffcc00;
                    }}
                """)
                record_btn.clicked.connect(lambda checked, vid=video_id, dur=video_duration:
                                           self.record_watch(vid, dur))
                self.videos_table.setCellWidget(i, 5, record_btn)

            self.videos_table.resizeColumnsToContents()
        except Exception as e:
            print(f"加载视频数据出错: {e}")

    def add_video(self):
        if self.course_combo.count() == 0:
            QMessageBox.warning(self, "提示", "请先添加课程！")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("添加视频")
        dialog.resize(500, 280)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        title_input = QLineEdit()
        title_input.setPlaceholderText("请输入视频标题")
        url_input = QLineEdit()
        url_input.setPlaceholderText("请输入视频链接（本地路径或网络URL）")
        duration_input = QLineEdit()
        duration_input.setPlaceholderText("请输入时长（秒）")
        sort_input = QLineEdit()
        sort_input.setPlaceholderText("请输入排序数字，越小越靠前")

        layout.addRow("视频标题 *:", title_input)
        layout.addRow("视频链接:", url_input)
        layout.addRow("时长(秒):", duration_input)
        layout.addRow("排序:", sort_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted and title_input.text().strip():
            try:
                engine = get_engine()
                duration = int(duration_input.text()) if duration_input.text() else 0
                sort_order = int(sort_input.text()) if sort_input.text() else 0
                df = pd.DataFrame([{
                    'course_id': self.course_combo.currentData(),
                    'title': title_input.text(),
                    'url': url_input.text(),
                    'duration': duration,
                    'sort_order': sort_order
                }])
                df.to_sql('videos', engine, if_exists='append', index=False)
                QMessageBox.information(self, "成功", "视频添加成功！")
                self.load_videos_by_course()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"添加失败：{e}")

    def edit_video(self):
        current_row = self.videos_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "提示", "请先选择要编辑的视频")
            return

        video_id = self.videos_table.item(current_row, 0).text()
        old_title = self.videos_table.item(current_row, 1).text()
        old_duration = self.videos_table.item(current_row, 2).text()
        old_sort = self.videos_table.item(current_row, 3).text()

        dialog = QDialog(self)
        dialog.setWindowTitle(f"编辑视频 - {old_title}")
        dialog.resize(500, 250)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        title_input = QLineEdit(old_title)
        duration_input = QLineEdit(old_duration)
        sort_input = QLineEdit(old_sort)

        layout.addRow("视频标题 *:", title_input)
        layout.addRow("时长(秒):", duration_input)
        layout.addRow("排序:", sort_input)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted and title_input.text().strip():
            try:
                engine = get_engine()
                duration = int(duration_input.text()) if duration_input.text() else 0
                sort_order = int(sort_input.text()) if sort_input.text() else 0
                with engine.connect() as conn:
                    conn.execute(text(f"""
                        UPDATE videos 
                        SET title = '{title_input.text()}',
                            duration = {duration},
                            sort_order = {sort_order}
                        WHERE id = {video_id}
                    """))
                    conn.commit()
                QMessageBox.information(self, "成功", "视频修改成功！")
                self.load_videos_by_course()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"修改失败：{e}")

    def delete_video(self):
        current_row = self.videos_table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "提示", "请先选择要删除的视频")
            return

        video_id = self.videos_table.item(current_row, 0).text()
        video_title = self.videos_table.item(current_row, 1).text()

        reply = QMessageBox.question(self, "确认", f"确定要删除视频【{video_title}】吗？",
                                     QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                engine = get_engine()
                with engine.connect() as conn:
                    conn.execute(text(f"DELETE FROM videos WHERE id = {video_id}"))
                    conn.commit()
                QMessageBox.information(self, "成功", "删除成功！")
                self.load_videos_by_course()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"删除失败：{e}")

    def play_video(self, url, video_id=None, video_duration=None):
        """播放视频并记录学习进度"""
        if not url or url == 'nan' or url == '':
            QMessageBox.warning(self, "提示", "该视频没有链接！")
            return

        # 播放视频
        try:
            if os.path.exists(url):
                os.startfile(url)
            else:
                import webbrowser
                webbrowser.open(url)
        except Exception as e:
            QMessageBox.warning(self, "提示", f"无法播放视频: {e}")
            return

        # 自动记录观看（如果有视频ID且在学习记录页面选择了学员）
        if video_id and hasattr(self, 'student_combo') and self.student_combo.currentIndex() >= 0:
            student_id = self.student_combo.currentData()
            if student_id:
                self._save_watch_record(student_id, video_id, video_duration)

    def record_watch(self, video_id, video_duration):
        """手动记录观看"""
        if not hasattr(self, 'student_combo') or self.student_combo.currentIndex() < 0:
            QMessageBox.warning(self, "提示", "请先在【学习记录】页面选择学员！")
            self.tab_widget.setCurrentIndex(3)  # 切换到学习记录页面
            return

        student_id = self.student_combo.currentData()
        if not student_id:
            QMessageBox.warning(self, "提示", "请先在【学习记录】页面选择学员！")
            return

        self._save_watch_record(student_id, video_id, video_duration)

    def _save_watch_record(self, student_id, video_id, video_duration):
        """保存观看记录"""
        try:
            engine = get_engine()
            with engine.connect() as conn:
                # 检查是否已有记录
                result = conn.execute(text(f"""
                    SELECT id, watch_count FROM learning_record 
                    WHERE student_id = {student_id} AND video_id = {video_id}
                """))
                existing = result.fetchone()

                if existing:
                    # 更新现有记录
                    conn.execute(text(f"""
                        UPDATE learning_record 
                        SET watch_count = watch_count + 1,
                            watched_seconds = {video_duration if video_duration else 0},
                            is_completed = 1,
                            last_watch_time = NOW()
                        WHERE student_id = {student_id} AND video_id = {video_id}
                    """))
                else:
                    # 创建新记录
                    conn.execute(text(f"""
                        INSERT INTO learning_record (student_id, video_id, watched_seconds, is_completed, last_watch_time, watch_count)
                        VALUES ({student_id}, {video_id}, {video_duration if video_duration else 0}, 1, NOW(), 1)
                    """))
                conn.commit()

            # 刷新学习记录显示
            if hasattr(self, 'load_learning_records'):
                self.load_learning_records()

            QMessageBox.information(self, "成功", "观看记录已保存！")
        except Exception as e:
            QMessageBox.warning(self, "错误", f"记录保存失败：{e}")

    # ==================== 学习记录 ====================
    def show_learning_records(self):
        self.clear_layout(self.learning_tab)

        layout = QVBoxLayout(self.learning_tab)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        select_layout = QHBoxLayout()
        label = QLabel("👤 选择学员:")
        label.setStyleSheet(
            f"color: {COLORS['primary']}; font-weight: bold; font-size: 14px; background: transparent;")
        select_layout.addWidget(label)

        # ========== 学员选择下拉框 - 单独设置样式 ==========
        self.student_combo = QComboBox()
        self.student_combo.setMinimumWidth(200)
        self.student_combo.setStyleSheet("""
            QComboBox {
                background-color: #0f1a2e;
                color: #eeeeee;
                border: 1px solid #0f3460;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #ff6b6b;
                margin-right: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #0f1a2e;
                color: #eeeeee;
                selection-background-color: #ff6b6b;
                selection-color: white;
                border: 1px solid #0f3460;
            }
            QComboBox QAbstractItemView::item {
                padding: 8px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #ee5a5a;
                color: white;
            }
        """)

        try:
            engine = get_engine()
            students_df = pd.read_sql("SELECT id, name FROM students", engine)
            for _, row in students_df.iterrows():
                self.student_combo.addItem(row['name'], row['id'])
        except Exception as e:
            print(f"加载学员列表出错: {e}")

        self.student_combo.currentIndexChanged.connect(self.load_learning_records)
        select_layout.addWidget(self.student_combo)
        select_layout.addStretch()

        btn_refresh = QPushButton("🔄 刷新")
        btn_refresh.setCursor(Qt.PointingHandCursor)
        btn_refresh.clicked.connect(lambda: self.load_learning_records())
        select_layout.addWidget(btn_refresh)

        layout.addLayout(select_layout)

        self.learning_table = QTableWidget()
        self.learning_table.setAlternatingRowColors(True)
        self.learning_table.setColumnCount(5)
        self.learning_table.setHorizontalHeaderLabels(["视频ID", "视频标题", "已观看(秒)", "完成状态", "观看次数"])
        self.learning_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.learning_table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.learning_table)

        if self.student_combo.count() > 0:
            self.load_learning_records()

    def load_learning_records(self):
        if self.student_combo.currentIndex() < 0 or self.student_combo.count() == 0:
            return

        student_id = self.student_combo.currentData()
        try:
            engine = get_engine()
            sql = f"""
            SELECT lr.video_id, v.title, lr.watched_seconds, lr.is_completed, lr.watch_count
            FROM learning_record lr
            JOIN videos v ON lr.video_id = v.id
            WHERE lr.student_id = {student_id}
            """
            df = pd.read_sql(sql, engine)

            self.learning_table.setRowCount(len(df))
            for i in range(len(df)):
                row = df.iloc[i]
                self.learning_table.setItem(i, 0,
                                            QTableWidgetItem(str(row['video_id']) if pd.notna(row['video_id']) else ""))
                self.learning_table.setItem(i, 1,
                                            QTableWidgetItem(str(row['title']) if pd.notna(row['title']) else ""))
                self.learning_table.setItem(i, 2, QTableWidgetItem(
                    str(row['watched_seconds']) if pd.notna(row['watched_seconds']) else "0"))
                completed = "✅ 已完成" if row['is_completed'] else "🔄 学习中"
                self.learning_table.setItem(i, 3, QTableWidgetItem(completed))
                self.learning_table.setItem(i, 4, QTableWidgetItem(
                    str(row['watch_count']) if pd.notna(row['watch_count']) else "0"))

            self.learning_table.resizeColumnsToContents()
        except Exception as e:
            print(f"加载学习记录出错: {e}")
            self.learning_table.setRowCount(0)

    # ==================== 作业管理 ====================
    def show_assignments(self):
        self.clear_layout(self.assignments_tab)

        layout = QVBoxLayout(self.assignments_tab)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        select_layout = QHBoxLayout()
        label = QLabel("👤 选择学员:")
        label.setStyleSheet(
            f"color: {COLORS['primary']}; font-weight: bold; font-size: 14px; background: transparent;")
        select_layout.addWidget(label)

        # ========== 作业学员选择下拉框 - 单独设置样式 ==========
        self.assignment_student_combo = QComboBox()
        self.assignment_student_combo.setMinimumWidth(200)
        self.assignment_student_combo.setStyleSheet("""
            QComboBox {
                background-color: #0f1a2e;
                color: #eeeeee;
                border: 1px solid #0f3460;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #ff6b6b;
                margin-right: 5px;
            }
            QComboBox QAbstractItemView {
                background-color: #0f1a2e;
                color: #eeeeee;
                selection-background-color: #ff6b6b;
                selection-color: white;
                border: 1px solid #0f3460;
            }
            QComboBox QAbstractItemView::item {
                padding: 8px;
            }
            QComboBox QAbstractItemView::item:hover {
                background-color: #ee5a5a;
                color: white;
            }
        """)

        try:
            engine = get_engine()
            students_df = pd.read_sql("SELECT id, name FROM students", engine)
            for _, row in students_df.iterrows():
                self.assignment_student_combo.addItem(row['name'], row['id'])
        except Exception as e:
            print(f"加载学员列表出错: {e}")

        self.assignment_student_combo.currentIndexChanged.connect(self.load_assignments)
        select_layout.addWidget(self.assignment_student_combo)
        select_layout.addStretch()

        btn_add = QPushButton("📤 提交作业")
        btn_add.setCursor(Qt.PointingHandCursor)
        btn_add.clicked.connect(self.submit_assignment)
        select_layout.addWidget(btn_add)

        btn_refresh = QPushButton("🔄 刷新")
        btn_refresh.setCursor(Qt.PointingHandCursor)
        btn_refresh.clicked.connect(lambda: self.load_assignments())
        select_layout.addWidget(btn_refresh)

        layout.addLayout(select_layout)

        self.assignments_table = QTableWidget()
        self.assignments_table.setAlternatingRowColors(True)
        self.assignments_table.setColumnCount(7)
        self.assignments_table.setHorizontalHeaderLabels(
            ["ID", "视频ID", "作业视频", "提交时间", "评分", "状态", "操作"])
        self.assignments_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.assignments_table.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.assignments_table)

        if self.assignment_student_combo.count() > 0:
            self.load_assignments()

    def load_assignments(self):
        if self.assignment_student_combo.currentIndex() < 0 or self.assignment_student_combo.count() == 0:
            return

        student_id = self.assignment_student_combo.currentData()
        try:
            engine = get_engine()
            df = pd.read_sql(f"SELECT * FROM assignments WHERE student_id = {student_id} ORDER BY id DESC", engine)

            self.assignments_table.setRowCount(len(df))
            for i in range(len(df)):
                row = df.iloc[i]
                self.assignments_table.setItem(i, 0, QTableWidgetItem(str(row['id']) if pd.notna(row['id']) else ""))
                self.assignments_table.setItem(i, 1, QTableWidgetItem(
                    str(row['video_id']) if pd.notna(row['video_id']) else ""))

                video_url = row['video_url'] if pd.notna(row['video_url']) else ''
                play_btn = QPushButton("▶ 播放作业")
                play_btn.setCursor(Qt.PointingHandCursor)
                play_btn.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {COLORS['success']};
                        color: white;
                        padding: 5px 15px;
                        border-radius: 6px;
                    }}
                    QPushButton:hover {{
                        background-color: #3dbdb5;
                    }}
                """)

                full_video_path = video_url
                if video_url and not os.path.isabs(video_url):
                    full_video_path = os.path.join(os.getcwd(), video_url)

                play_btn.clicked.connect(
                    lambda checked, url=full_video_path, original_url=video_url: self.play_assignment_video(url,
                                                                                                            original_url))
                self.assignments_table.setCellWidget(i, 2, play_btn)

                self.assignments_table.setItem(i, 3, QTableWidgetItem(
                    str(row['submit_time']) if pd.notna(row['submit_time']) else ""))
                score_val = str(row['score']) if pd.notna(row['score']) else "未评分"
                self.assignments_table.setItem(i, 4, QTableWidgetItem(score_val))
                self.assignments_table.setItem(i, 5, QTableWidgetItem(
                    str(row['status']) if pd.notna(row['status']) else "待批改"))

                grade_btn = QPushButton("✏️ 评分/点评")
                grade_btn.setCursor(Qt.PointingHandCursor)
                grade_btn.clicked.connect(lambda checked, assignment_id=row['id']: self.grade_assignment(assignment_id))
                self.assignments_table.setCellWidget(i, 6, grade_btn)

            self.assignments_table.resizeColumnsToContents()
        except Exception as e:
            print(f"加载作业数据出错: {e}")

    def submit_assignment(self):
        if self.assignment_student_combo.count() == 0:
            QMessageBox.warning(self, "提示", "请先添加学员！")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("提交作业")
        dialog.resize(600, 450)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        video_id_input = QLineEdit()
        video_id_input.setPlaceholderText("请输入视频ID（可选）")

        file_layout = QHBoxLayout()
        video_path_input = QLineEdit()
        video_path_input.setPlaceholderText("请选择本地视频文件")
        video_path_input.setReadOnly(True)
        btn_browse = QPushButton("📁 浏览")
        btn_browse.setCursor(Qt.PointingHandCursor)
        file_layout.addWidget(video_path_input)
        file_layout.addWidget(btn_browse)

        desc_input = QTextEdit()
        desc_input.setMaximumHeight(120)
        desc_input.setPlaceholderText("请输入作业说明...")

        layout.addRow("关联视频ID:", video_id_input)
        layout.addRow("作业视频:", file_layout)
        layout.addRow("作业说明:", desc_input)

        def browse_file():
            file_path, _ = QFileDialog.getOpenFileName(
                dialog, "选择作业视频", "",
                "视频文件 (*.mp4 *.avi *.mov *.mkv *.flv *.wmv);;所有文件 (*.*)"
            )
            if file_path:
                video_path_input.setText(file_path)

        btn_browse.clicked.connect(browse_file)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted:
            video_path = video_path_input.text()

            if not video_path.strip():
                QMessageBox.warning(self, "提示", "请选择作业视频文件！")
                return

            if not os.path.exists(video_path):
                QMessageBox.warning(self, "提示", "视频文件不存在！")
                return

            try:
                student_id = self.assignment_student_combo.currentData()
                student_name = self.assignment_student_combo.currentText()
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_extension = os.path.splitext(video_path)[1]
                new_filename = f"{student_id}_{student_name}_{timestamp}{file_extension}"
                new_filepath = os.path.join(self.video_save_dir, new_filename)

                shutil.copy2(video_path, new_filepath)
                video_url = f"assignments_videos/{new_filename}"

                engine = get_engine()
                video_id = int(video_id_input.text()) if video_id_input.text() else None
                df = pd.DataFrame([{
                    'student_id': student_id,
                    'video_id': video_id,
                    'video_url': video_url,
                    'description': desc_input.toPlainText(),
                    'submit_time': datetime.now(),
                    'status': '待批改'
                }])
                df.to_sql('assignments', engine, if_exists='append', index=False)
                QMessageBox.information(self, "成功", f"作业提交成功！")
                self.load_assignments()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"提交失败：{e}")

    def play_assignment_video(self, video_path, original_url):
        if not video_path or video_path == 'nan':
            QMessageBox.warning(self, "提示", "该作业没有视频文件！")
            return

        if os.path.exists(video_path):
            try:
                os.startfile(video_path)
            except Exception as e:
                QMessageBox.warning(self, "提示", f"无法播放视频：{e}")
        else:
            if original_url and original_url.startswith('http'):
                import webbrowser
                webbrowser.open(original_url)
            else:
                QMessageBox.warning(self, "提示", f"视频文件不存在：{video_path}")

    def grade_assignment(self, assignment_id):
        dialog = QDialog(self)
        dialog.setWindowTitle("作业评分与点评")
        dialog.resize(450, 350)
        dialog.setStyleSheet(GLOBAL_STYLE)

        layout = QFormLayout(dialog)
        layout.setSpacing(15)
        layout.setContentsMargins(25, 25, 25, 25)

        try:
            engine = get_engine()
            df = pd.read_sql(f"SELECT * FROM assignments WHERE id = {assignment_id}", engine)
            if len(df) == 0:
                return
            row = df.iloc[0]
            current_score = row['score'] if pd.notna(row['score']) else ""
            current_comment = row['teacher_comment'] if pd.notna(row['teacher_comment']) else ""
            current_status = row['status'] if pd.notna(row['status']) else "待批改"
        except Exception as e:
            print(f"获取作业信息出错: {e}")
            return

        score_slider = QSlider(Qt.Horizontal)
        score_slider.setRange(0, 10)
        score_slider.setValue(int(current_score) if current_score else 0)
        score_slider.setTickPosition(QSlider.TicksBelow)
        score_slider.setTickInterval(1)

        score_label = QLabel(f"当前评分：{score_slider.value()}")
        score_label.setStyleSheet(f"color: {COLORS['primary']}; font-weight: bold; font-size: 14px;")
        score_slider.valueChanged.connect(lambda v: score_label.setText(f"当前评分：{v}"))

        comment_input = QTextEdit()
        comment_input.setPlainText(str(current_comment) if current_comment else "")
        comment_input.setPlaceholderText("请输入老师点评...")

        status_combo = QComboBox()
        status_combo.addItems(["待批改", "已批改"])
        status_index = status_combo.findText(str(current_status))
        if status_index >= 0:
            status_combo.setCurrentIndex(status_index)

        layout.addRow("评分 (0-10):", score_slider)
        layout.addRow("", score_label)
        layout.addRow("老师点评:", comment_input)
        layout.addRow("状态:", status_combo)

        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(dialog.accept)
        buttons.rejected.connect(dialog.reject)
        layout.addRow(buttons)

        if dialog.exec() == QDialog.Accepted:
            try:
                engine = get_engine()
                with engine.connect() as conn:
                    conn.execute(text(f"""
                        UPDATE assignments 
                        SET score = {score_slider.value()},
                            teacher_comment = '{comment_input.toPlainText()}',
                            status = '{status_combo.currentText()}'
                        WHERE id = {assignment_id}
                    """))
                    conn.commit()
                QMessageBox.information(self, "成功", "评分和点评已保存！")
                self.load_assignments()
            except Exception as e:
                QMessageBox.warning(self, "错误", f"保存失败：{e}")


# ==================== 主程序入口 ====================
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    font = QFont("Microsoft YaHei", 10)
    app.setFont(font)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())