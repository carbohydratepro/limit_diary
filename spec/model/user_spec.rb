# encoding: utf-8
require 'rails_helper'

RSpec.describe User, type: :model do
  describe "バリデーションのテスト" do
    subject { user.valid? }

    let!(:other_user) { create(:user) }
    let(:user) { build(:user) }

    context 'nameカラム' do
      it "名前が空欄でないこと" do
        user.name = ""
        is_expected.to eq false
      end
      it '2文字以上であること: 1文字は×' do
        user.name = Faker::Lorem.characters(number: 1)
        is_expected.to eq false
      end
      it '2文字以上であること: 2文字は〇' do
        user.name = Faker::Lorem.characters(number: 2)
        is_expected.to eq true
      end
      it "パスワードが6文字以上であること" do
        user.password = "12345"
        expect(user).to_not be_valid
      end
      it '一意性があること' do
        user.name = other_user.name
        is_expected.to eq false
      end
    end
    context 'emailカラム' do
      it "メールが空欄でないこと" do
        user = User.new(name: "Test User")
        expect(user).to_not be_valid
      end
      it "メールではない文字列でないこと" do
        user = User.new(name: "test User", email: "test mail")
        expect(user).to_not be_valid
      end
    end
  end

  describe 'アソシエーションのテスト' do
    context 'Blogモデルとの関係' do
      it '1:Nとなっている' do
        expect(User.reflect_on_association(:blogs).macro).to eq :has_many
      end
    end
    context 'Favoriteモデルとの関係' do
      it '1:Nとなっている' do
        expect(User.reflect_on_association(:favorites).macro).to eq :has_many
      end
    end
  end
end
